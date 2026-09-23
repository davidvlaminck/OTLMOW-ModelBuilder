from otlmow_modelbuilder.GeometrieInheritanceProcessor import GeometrieInheritanceProcessor
from otlmow_modelbuilder.GeometrieType import GeometrieType
from otlmow_modelbuilder.SQLDataClasses.Inheritance import Inheritance
from otlmow_modelbuilder.SQLDataClasses.OSLOClass import OSLOClass

NS = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatielement'

A_URI = f'{NS}#A'
B_URI = f'{NS}#B'
C_URI = f'{NS}#C'
D_URI = f'{NS}#D'


def get_test_data_multi_child():
    classes = [
        OSLOClass(label='A', name='A', objectUri=A_URI, definition='', usagenote='',
                  abstract=0, deprecated_version=''),
        OSLOClass(label='B', name='B', objectUri=B_URI, definition='', usagenote='',
                  abstract=0, deprecated_version=''),
        OSLOClass(label='C', name='C', objectUri=C_URI, definition='', usagenote='',
                  abstract=0, deprecated_version=''),
        OSLOClass(label='D', name='D', objectUri=D_URI, definition='', usagenote='',
                  abstract=1, deprecated_version=''),
    ]

    geometrie_types = [
        GeometrieType(objectUri=A_URI, label_nl='A',
                      geen_geometrie=0, punt3D=0, lijn3D=1, polygoon3D=1),
        GeometrieType(objectUri=B_URI, label_nl='B',
                      geen_geometrie=0, punt3D=0, lijn3D=1, polygoon3D=1),
        GeometrieType(objectUri=C_URI, label_nl='C',
                      geen_geometrie=0, punt3D=0, lijn3D=0, polygoon3D=1),
    ]

    inheritances = [
        Inheritance(base_name='D', base_uri=D_URI, class_name='A', class_uri=A_URI,
                    deprecated_version=''),
        Inheritance(base_name='D', base_uri=D_URI, class_name='B', class_uri=B_URI,
                    deprecated_version=''),
        Inheritance(base_name='D', base_uri=D_URI, class_name='C', class_uri=C_URI,
                    deprecated_version=''),
    ]

    return classes, geometrie_types, inheritances


def get_test_data():
    classes = [
        OSLOClass(label='A', name='A', objectUri=A_URI, definition='', usagenote='',
                  abstract=0, deprecated_version=''),
        OSLOClass(label='B', name='B', objectUri=B_URI, definition='', usagenote='',
                  abstract=0, deprecated_version=''),
        OSLOClass(label='C', name='C', objectUri=C_URI, definition='', usagenote='',
                  abstract=1, deprecated_version=''),
    ]

    geometrie_types = [
        GeometrieType(objectUri=A_URI, label_nl='A',
                      geen_geometrie=0, punt3D=1, lijn3D=1, polygoon3D=0),
        GeometrieType(objectUri=B_URI, label_nl='B',
                      geen_geometrie=0, punt3D=0, lijn3D=1, polygoon3D=1),
    ]

    inheritances = [
        Inheritance(base_name='C', base_uri=C_URI, class_name='A', class_uri=A_URI,
                    deprecated_version=''),
        Inheritance(base_name='C', base_uri=C_URI, class_name='B', class_uri=B_URI,
                    deprecated_version=''),
    ]

    return classes, geometrie_types, inheritances


def test_inherited_common_geometry_type():
    """
    Scenario:
    - Class A has geometry types: punt (PuntGeometrie) and lijn (LijnGeometrie)
    - Class B has geometry types: lijn (LijnGeometrie) and vlak (VlakGeometrie)
    - Class C is the abstract base class for both A and B

    The common geometry type between A and B is lijn. This should be moved to the
    base class C via inheritance. A keeps punt, B keeps vlak, C gets lijn.
    """
    classes, geometrie_types, inheritances = get_test_data()

    processor = GeometrieInheritanceProcessor(geometrie_types=geometrie_types,
                                              inheritances=inheritances,
                                              classes=classes)
    result = processor.process_inheritances()

    def find(uri):
        return next((g for g in result if g.objectUri == uri), None)

    geo_a = find(A_URI)
    geo_b = find(B_URI)
    geo_c = find(C_URI)

    assert geo_a is not None, 'A should still have a geometry type entry (with punt only)'
    assert geo_b is not None, 'B should still have a geometry type entry (with vlak only)'
    assert geo_c is not None, 'C should have a new geometry type entry (with lijn only)'

    assert geo_a.punt3D == 1 and geo_a.lijn3D == 0 and geo_a.polygoon3D == 0, \
        'A should only have punt'
    assert geo_b.polygoon3D == 1 and geo_b.punt3D == 0 and geo_b.lijn3D == 0, \
        'B should only have vlak'
    assert geo_c.lijn3D == 1 and geo_c.punt3D == 0 and geo_c.polygoon3D == 0, \
        'C should only have lijn'


def test_inherited_common_geometry_type_multi_child():
    """
    Scenario:
    - Class A has geometry types: lijn (LijnGeometrie) and vlak (VlakGeometrie)
    - Class B has geometry types: lijn (LijnGeometrie) and vlak (VlakGeometrie)
    - Class C has geometry types: vlak (VlakGeometrie)
    - Class D is the abstract base class for A, B and C

    The common geometry type between A, B and C is vlak. This should be moved to
    the base class D via inheritance. A keeps lijn, B keeps lijn and C gets nothing
    (its only type is inherited by D).
    """
    classes, geometrie_types, inheritances = get_test_data_multi_child()

    processor = GeometrieInheritanceProcessor(geometrie_types=geometrie_types,
                                              inheritances=inheritances,
                                              classes=classes)
    result = processor.process_inheritances()

    def find(uri):
        return next((g for g in result if g.objectUri == uri), None)

    geo_a = find(A_URI)
    geo_b = find(B_URI)
    geo_c = find(C_URI)
    geo_d = find(D_URI)

    assert geo_d is not None, 'D should have a new geometry type entry (with vlak only)'
    assert geo_a is not None, 'A should still have a geometry type entry (with lijn only)'
    assert geo_b is not None, 'B should still have a geometry type entry (with lijn only)'
    assert geo_c is None or (geo_c.geen_geometrie != 1 and geo_c.punt3D != 1 and
                             geo_c.lijn3D != 1 and geo_c.polygoon3D != 1), \
        'C should have no geometry type (only inherited from D)'

    assert geo_d.polygoon3D == 1 and geo_d.lijn3D == 0 and geo_d.punt3D == 0, \
        'D should only have vlak'
    assert geo_a.lijn3D == 1 and geo_a.polygoon3D == 0 and geo_a.punt3D == 0, \
        'A should only have lijn'
    assert geo_b.lijn3D == 1 and geo_b.polygoon3D == 0 and geo_b.punt3D == 0, \
        'B should only have lijn'
