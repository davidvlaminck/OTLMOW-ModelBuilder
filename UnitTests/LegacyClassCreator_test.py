import os

from otlmow_modelbuilder.LegacyClassCreator import LegacyClassCreator

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


expectedDataAB = ['# coding=utf-8',
    'from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import LegacyObject',
    '', '',
    '# Generated with LegacyClassCreator. To modify: extend, do not edit',
    'class AB(LegacyObject):',
    '    """Afstandsbewaking (Legacy)\n\tAfstandsbewaking"""',
    '',
    "    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#AB'",
    '    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""',
    '',
    '    def __init__(self):',
    '        super().__init__()']


def test_AB():
    creator = LegacyClassCreator()
    csv_row = [
        'https://lgc.data.wegenenverkeer.be/ns/installatie#AB','Afstandsbewaking (Legacy)','AB','Afstandsbewaking']
    data_to_write = creator.create_blocks_to_write_from_rows(csv_row)
    assert data_to_write == expectedDataAB
