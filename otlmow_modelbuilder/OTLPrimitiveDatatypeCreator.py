import logging
import re

from otlmow_modelbuilder.AbstractDatatypeCreator import AbstractDatatypeCreator
from otlmow_modelbuilder.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypePrimitive import OSLODatatypePrimitive


class OTLPrimitiveDatatypeCreator(AbstractDatatypeCreator):
    def __init__(self, oslo_collector: OSLOCollector):
        super().__init__(oslo_collector)
        logging.info("Created an instance of OTLPrimitiveDatatypeCreator")

    def create_block_to_write_from_primitive_types(self, oslo_datatype_primitive: OSLODatatypePrimitive,
                                                   primitive_datatype_validation_rules,
                                                   model_location: str = '') -> [str]:
        if not isinstance(oslo_datatype_primitive, OSLODatatypePrimitive):
            raise ValueError(f"Input is not a OSLODatatypePrimitive")

        if oslo_datatype_primitive.objectUri == '':
            raise ValueError(f"OSLODatatypePrimitive.objectUri is invalid. Value = '{oslo_datatype_primitive.objectUri}'")

        if oslo_datatype_primitive.objectUri in primitive_datatype_validation_rules['valid_uri_and_types'].keys():
            pass
        else:
            match_re = False
            for regex in primitive_datatype_validation_rules["valid_regexes"]:
                match_re = re.match(pattern=regex, string=oslo_datatype_primitive.objectUri)
                if match_re:
                    break
            if not match_re:
                raise ValueError(
                    f"OSLODatatypePrimitive.objectUri is invalid. Value = '{oslo_datatype_primitive.objectUri}'")

        if oslo_datatype_primitive.name == '':
            raise ValueError(f"OSLODatatypePrimitive.name is invalid. Value = '{oslo_datatype_primitive.name}'")

        if '#KwantWrd' in oslo_datatype_primitive.objectUri:
            return self.create_block_to_write_from_complex_primitive_or_union_types(
                oslo_datatype=oslo_datatype_primitive,
                type_field='KwantWrd',
                model_location=model_location)
        if '#Dte' in oslo_datatype_primitive.objectUri:
            return self.create_block_to_write_from_complex_primitive_or_union_types(
                oslo_datatype=oslo_datatype_primitive,
                type_field='Primitive',
                model_location=model_location)
