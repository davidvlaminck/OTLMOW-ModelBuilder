import logging

from otlmow_modelbuilder.AbstractDatatypeCreator import AbstractDatatypeCreator
from otlmow_modelbuilder.SQLDataClasses.OSLOCollector import OSLOCollector
from otlmow_modelbuilder.SQLDataClasses.OSLODatatypeComplex import OSLODatatypeComplex


class OTLComplexDatatypeCreator(AbstractDatatypeCreator):
    def __init__(self, oslo_collector: OSLOCollector):
        super().__init__(oslo_collector)
        logging.info("Created an instance of OTLComplexDatatypeCreator")

    def create_block_to_write_from_complex_types(self, oslo_datatype_complex: OSLODatatypeComplex, model_location='') -> [str]:
        if not isinstance(oslo_datatype_complex, OSLODatatypeComplex):
            raise ValueError(f"Input is not a OSLODatatypeComplex")

        if oslo_datatype_complex.objectUri == '' or not (oslo_datatype_complex.objectUri == 'https://schema.org/ContactPoint' or
                                                         oslo_datatype_complex.objectUri == 'https://schema.org/OpeningHoursSpecification' or
                                                         (oslo_datatype_complex.objectUri.startswith(
                                                           'https://wegenenverkeer.data.vlaanderen.be/ns/') and 'Dtc' in oslo_datatype_complex.objectUri)):
            raise ValueError(f"OSLODatatypeComplex.objectUri is invalid. Value = '{oslo_datatype_complex.objectUri}'")

        if oslo_datatype_complex.name == '':
            raise ValueError(f"OSLODatatypeComplex.name is invalid. Value = '{oslo_datatype_complex.name}'")

        if oslo_datatype_complex.objectUri.startswith(
                'https://wegenenverkeer.data.vlaanderen.be/ns/') and 'Dtc' in oslo_datatype_complex.objectUri:
            return self.create_block_to_write_from_complex_primitive_or_union_types(oslo_datatype_complex, type_field='Complex',
                                                                                    model_location=model_location)
        elif oslo_datatype_complex.objectUri.startswith('https://schema.org/'):
            return self.create_block_to_write_from_complex_primitive_or_union_types(oslo_datatype_complex, type_field='Complex',
                                                                                    model_location=model_location)
        else:
            raise NotImplementedError

    @staticmethod
    def get_unit_from_constraints(constraints: str) -> str:
        if constraints == '':
            raise ValueError
        split_text = constraints.split('"')
        return split_text[1]
