import logging

from otlmow_modelbuilder.AbstractDatatypeCreator import AbstractDatatypeCreator
from otlmow_modelbuilder.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.OSLODatatypePrimitive import OSLODatatypePrimitive


class OTLPrimitiveDatatypeCreator(AbstractDatatypeCreator):
    def __init__(self, osloCollector: OSLOCollector):
        super().__init__(osloCollector)
        logging.info("Created an instance of OTLPrimitiveDatatypeCreator")

    def create_block_to_write_from_primitive_types(self, osloDatatypePrimitive: OSLODatatypePrimitive, model_location=''):
        if not isinstance(osloDatatypePrimitive, OSLODatatypePrimitive):
            raise ValueError(f"Input is not a OSLODatatypePrimitive")
        if osloDatatypePrimitive.objectUri == '' or not (osloDatatypePrimitive.objectUri.startswith('http://www.w3.org/200') or
                                                         osloDatatypePrimitive.objectUri.startswith(
                                                             'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Dte')
                                                         or osloDatatypePrimitive.objectUri.startswith(
                    'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrd')):
            raise ValueError(f"OSLODatatypePrimitive.objectUri is invalid. Value = '{osloDatatypePrimitive.objectUri}'")
        if osloDatatypePrimitive.name == '':
            raise ValueError(f"OSLODatatypePrimitive.name is invalid. Value = '{osloDatatypePrimitive.name}'")

        if osloDatatypePrimitive.objectUri.startswith(
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrd'):
            return self.create_block_to_write_from_complex_primitive_or_union_types(osloDatatypePrimitive,
                                                                                    typeField='KwantWrd',
                                                                                    model_location=model_location)
        if osloDatatypePrimitive.objectUri.startswith('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Dte'):
            return self.create_block_to_write_from_complex_primitive_or_union_types(osloDatatypePrimitive,
                                                                                    typeField='Primitive',
                                                                                    model_location=model_location)
