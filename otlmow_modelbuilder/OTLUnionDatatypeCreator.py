import logging

from otlmow_modelbuilder.AbstractDatatypeCreator import AbstractDatatypeCreator
from otlmow_modelbuilder.SQLDataClasses.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypeUnion import OSLODatatypeUnion


class OTLUnionDatatypeCreator(AbstractDatatypeCreator):
    def __init__(self, oslo_collector: OSLOCollector):
        super().__init__(oslo_collector)
        logging.info("Created an instance of OTLUnionDatatypeCreator")

    def create_block_to_write_from_union_types(self, union_datatype: OSLODatatypeUnion,
                                               model_location: str = '') -> [str]:
        if not isinstance(union_datatype, OSLODatatypeUnion):
            raise ValueError(f"Input is not a OSLODatatypeUnion")

        if union_datatype.objectUri == '' or not (union_datatype.objectUri.startswith(
                'https://wegenenverkeer.data.vlaanderen.be/ns/') and 'Dtu' in union_datatype.objectUri):
            raise ValueError(f"OSLODatatypeUnion.objectUri is invalid. Value = '{union_datatype.objectUri}'")

        if union_datatype.name == '':
            raise ValueError(f"OSLODatatypeUnion.name is invalid. Value = '{union_datatype.name}'")

        return self.create_block_to_write_from_complex_primitive_or_union_types(oslo_datatype=union_datatype,
                                                                                type_field='UnionType',
                                                                                model_location=model_location)
