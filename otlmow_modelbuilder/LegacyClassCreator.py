import logging

from otlmow_modelbuilder.AbstractDatatypeCreator import AbstractDatatypeCreator


class LegacyClassCreator(AbstractDatatypeCreator):
    def __init__(self):
        super().__init__(None)
        logging.info("Created an instance of LegacyClassCreator")


    def create_blocks_to_write_from_rows(self, lgc_type_row: [str], model_location='') -> [str]:
        try:
            legacy_uri = lgc_type_row[0]
            legacy_name = lgc_type_row[2]
            legacy_definition = lgc_type_row[1] + "\n\t" + lgc_type_row[3]
        except Exception as e:
            logging.error(f"Error in create_blocks_to_write_from_rows: {e}")
            raise e

        if '.' in legacy_name:
            legacy_name = legacy_name.replace('.', '_')
        if '-' in legacy_name:
            legacy_name = legacy_name.replace('-', '_')
        if legacy_name == "RIS":
            legacy_name = "RISLegacy"
        elif legacy_name == 'Fietstel':
            legacy_name = 'FietstelLegacy'
        elif legacy_name == 'Brug':
            legacy_name = 'BeweegbareBrug'
        elif legacy_name == 'Voedingskeuzeschakelaar':
            legacy_name = 'VKS'

        if legacy_uri == '':
            raise ValueError(f"OSLOClass.objectUri is invalid. Value = '{legacy_uri}'")

        if legacy_name == '':
            raise ValueError(f"OSLOClass.name is invalid. Value = '{legacy_name}'")

        return self.create_block_from_class(legacy_uri=legacy_uri, legacy_name=legacy_name,
                                            legacy_definition=legacy_definition, model_location=model_location)

    def create_block_from_class(self, legacy_uri: str, legacy_name: str, legacy_definition: str,
                                model_location: str = '') -> [str]:
        return [
            '# coding=utf-8',
            'from otlmow_model.OtlmowModel.BaseClasses.LegacyObject import LegacyObject',
            '',
            '',
            f'# Generated with {self.__class__.__name__}. To modify: extend, do not edit',
            f'class {legacy_name}(LegacyObject):',
            f'    """{legacy_definition}"""',
            '',
            f"    typeURI = '{legacy_uri}'",
            '    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""',
            '',
            '    def __init__(self):',
            '        super().__init__()',
        ]
