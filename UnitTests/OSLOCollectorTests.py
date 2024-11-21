from pathlib import Path

from otlmow_modelbuilder.OSLOCollector import OSLOCollector

current_file_path = Path(__file__)
base_dir = current_file_path.parent
test_classes_subset_location = Path(f'{base_dir}/OTL_AllCasesTestClass.db')


def test_find_superclasses_uri_by_class_uri_using_testmodel():
    subset_collector = OSLOCollector(test_classes_subset_location)
    subset_collector.collect_all()

    aim_object_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject'
    subclasses = subset_collector.find_subclasses_uri_by_class_uri(aim_object_uri)
    assert subclasses == ['https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
                            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnotherTestClass',
                            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DeprecatedTestClass']

    relatie_object_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject'
    subclasses = subset_collector.find_subclasses_uri_by_class_uri(relatie_object_uri)
    assert subclasses == ['https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DirectioneleRelatie',
                          'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NietDirectioneleRelatie']

def test_find_indirect_superclasses_uri_by_class_uri_using_testmodel():
    subset_collector = OSLOCollector(test_classes_subset_location)
    subset_collector.collect_all()

    relatie_object_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject'
    subclasses = subset_collector.find_indirect_subclasses_uri_by_class_uri(relatie_object_uri)
    assert subclasses == ['https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DirectioneleRelatie',
                          'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NietDirectioneleRelatie',
                          'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging',
                          'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt']