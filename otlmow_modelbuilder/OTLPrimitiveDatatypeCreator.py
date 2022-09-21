import logging

from otlmow_modelbuilder.AbstractDatatypeCreator import AbstractDatatypeCreator
from otlmow_modelbuilder.SQLDataClasses.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypePrimitive import OSLODatatypePrimitive


class OTLPrimitiveDatatypeCreator(AbstractDatatypeCreator):
    def __init__(self, oslo_collector: OSLOCollector):
        super().__init__(oslo_collector)
        logging.info("Created an instance of OTLPrimitiveDatatypeCreator")

    def create_block_to_write_from_primitive_types(self, oslo_datatype_primitive: OSLODatatypePrimitive,
                                                   model_location: str = '') -> [str]:
        if not isinstance(oslo_datatype_primitive, OSLODatatypePrimitive):
            raise ValueError(f"Input is not a OSLODatatypePrimitive")
        if oslo_datatype_primitive.objectUri == '' or not (
                oslo_datatype_primitive.objectUri.startswith('http://www.w3.org/200') or
                oslo_datatype_primitive.objectUri.startswith(
                    'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Dte')
                or oslo_datatype_primitive.objectUri.startswith(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrd')):
            raise ValueError(
                f"OSLODatatypePrimitive.objectUri is invalid. Value = '{oslo_datatype_primitive.objectUri}'")
        if oslo_datatype_primitive.name == '':
            raise ValueError(f"OSLODatatypePrimitive.name is invalid. Value = '{oslo_datatype_primitive.name}'")

        if oslo_datatype_primitive.objectUri.startswith(
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrd'):
            return self.create_block_to_write_from_complex_primitive_or_union_types(
                oslo_datatype=oslo_datatype_primitive,
                type_field='KwantWrd',
                model_location=model_location)
        if oslo_datatype_primitive.objectUri.startswith(
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Dte'):
            return self.create_block_to_write_from_complex_primitive_or_union_types(
                oslo_datatype=oslo_datatype_primitive,
                type_field='Primitive',
                model_location=model_location)
