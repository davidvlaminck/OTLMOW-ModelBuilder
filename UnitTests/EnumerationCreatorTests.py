from pathlib import Path

from otlmow_modelbuilder._otlmow_modelbuilder_rs import (
    create_block_to_write_from_enumeration as rust_create_block,
)
from otlmow_modelbuilder._otlmow_modelbuilder_rs import (
    get_adm_status_from_ttl,
    get_keuzelijstwaardes_from_ttl,
)

from otlmow_modelbuilder.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.OTLEnumerationCreator import OTLEnumerationCreator

CURRENT_DIR = Path(__file__).parent


def set_up() -> OSLOCollector:
    file_location = CURRENT_DIR / 'OTL_AllCasesTestClass.db'
    collector = OSLOCollector(file_location)
    collector.collect_all()
    return collector


enumeration_validation_rules = {
    "valid_uri_and_types": {},
    "valid_regexes": ["^https://wegenenverkeer.data.vlaanderen.be/ns/.+#Kl.+"]
}


class TestCreateBlockEnumerationComparison:
    def test_keuzelijst_matches_python(self):
        from rdflib import Graph

        collector = set_up()

        ttl_path = str(CURRENT_DIR / 'kl_testkeuzelijst' / 'KlTestKeuzelijst.ttl')

        rust_waardes = get_keuzelijstwaardes_from_ttl(ttl_path, 'spd')

        g = Graph()
        g.parse(ttl_path, format='turtle')
        python_waardes = OTLEnumerationCreator.get_keuzelijstwaardes_from_graph(g, 'spd')
        assert len(rust_waardes) == len(python_waardes)

        keuzelijst = collector.find_enumeration_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlTestKeuzelijst')

        adm_status = get_adm_status_from_ttl(
            ttl_path,
            'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTestKeuzelijst',
            'spd')

        with OTLEnumerationCreator(collector, env='unittest', enumeration_locations_by_environment={}) as creator:
            test_graph = creator.parse_files_in_dir_to_graph(directory=CURRENT_DIR)
            creator.graph_dict['prd'] = creator.parse_graph_to_dict(test_graph)

            python_result = creator.create_block_to_write_from_enumerations(
                keuzelijst,
                enumeration_validation_rules=enumeration_validation_rules,
                environment='prd')

            rust_result = rust_create_block(
                rust_waardes,
                adm_status,
                keuzelijst.name,
                keuzelijst.definition,
                keuzelijst.label,
                keuzelijst.objectUri,
                keuzelijst.codelist,
                keuzelijst.deprecated_version,
                "OTLEnumerationCreator")

            assert rust_result == python_result
