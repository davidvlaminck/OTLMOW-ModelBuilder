import logging
import re
from typing import Dict

from otlmow_modelbuilder.AbstractDatatypeCreator import AbstractDatatypeCreator
from otlmow_modelbuilder.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypeComplex import OSLODatatypeComplex


class OTLComplexDatatypeCreator(AbstractDatatypeCreator):
    def __init__(self, oslo_collector: OSLOCollector):
        super().__init__(oslo_collector)
        logging.info("Created an instance of OTLComplexDatatypeCreator")

    def create_block_to_write_from_complex_types(self, oslo_datatype_complex: OSLODatatypeComplex,
                                                 complex_datatype_validation_rules: Dict, model_location='') -> [str]:
        if not isinstance(oslo_datatype_complex, OSLODatatypeComplex):
            raise ValueError(f"Input is not a OSLODatatypeComplex")

        if oslo_datatype_complex.objectUri == '':
            raise ValueError(f"OSLODatatypeComplex.objectUri is invalid. Value = '{oslo_datatype_complex.objectUri}'")

        if oslo_datatype_complex.objectUri in complex_datatype_validation_rules['valid_uri_and_types'].keys():
            pass
        else:
            match_re = False
            for regex in complex_datatype_validation_rules["valid_regexes"]:
                match_re = re.match(pattern=regex, string=oslo_datatype_complex.objectUri)
                if match_re:
                    break
            if not match_re:
                raise ValueError(
                    f"OSLODatatypeComplex.objectUri is invalid. Value = '{oslo_datatype_complex.objectUri}'")

        if oslo_datatype_complex.name == '':
            raise ValueError(f"OSLODatatypeComplex.name is invalid. Value = '{oslo_datatype_complex.name}'")

        return self.create_block_to_write_from_complex_primitive_or_union_types(
            oslo_datatype_complex, type_field='Complex', model_location=model_location,
            valid_uri_and_types=complex_datatype_validation_rules['valid_uri_and_types'])

    @staticmethod
    def get_unit_from_constraints(constraints: str) -> str:
        if constraints == '':
            raise ValueError
        split_text = constraints.split('"')
        return split_text[1]
