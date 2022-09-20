from unittest import TestCase
from otlmow_modelbuilder.HelperFunctions import get_ns_and_name_from_uri, get_class_directory_from_ns, wrap_in_quotes


class HelperFunctionsTests(TestCase):
    def test_empty_string_returns_empty_string_in_single_quotes(self):
        result = wrap_in_quotes('')
        self.assertEqual("''", result)

    def test_none(self):
        with self.assertRaises(TypeError):
            # noinspection PyTypeChecker
            wrap_in_quotes(None)

    def test_string_without_quotes_returns_string_with_single_quotes(self):
        result = wrap_in_quotes('a')
        self.assertEqual("'a'", result)

    def test_string_with_single_quotes_returns_string_with_double_quotes(self):
        result = wrap_in_quotes("kado's")
        self.assertEqual('"kado\'s"', result)

    def test_string_with_double_quotes_returns_string_with_single_quotes(self):
        result = wrap_in_quotes('ik "test" dit uit')
        self.assertEqual('\'ik "test" dit uit\'', result)

    def test_string_with_more_doubles_than_singles_returns_string_with_single_quotes(self):
        result = wrap_in_quotes("ik \"test\" kado's uit")
        self.assertEqual("\'ik \"test\" kado\\\'s uit\'", result)

    def test_get_ns_and_name_from_uri_invalid_uris(self):
        agent_uri = 'http://purl.org/dc/terms/Agent'
        with self.assertRaises(ValueError):
            get_ns_and_name_from_uri(agent_uri)

    def test_get_ns_and_name_from_uri_valid_uris(self):
        testset = {
            'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AOWSType': ('abstracten', 'AOWSType'),
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#ActivityComplex': (
                'implementatieelement', 'ActivityComplex'),
            'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aardingsinstallatie': (
                'installatie', 'Aardingsinstallatie'),
            'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerHoutigeVegetatie': (
                'levenscyclus', 'BeheerHoutigeVegetatie'),
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera': ('onderdeel', 'ANPRCamera'),
            'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#Keuring': ('proefenmeting', 'Keuring')
        }

        for uri, expected_tuple in testset.items():
            with self.subTest(f'get_ns_and_name_from {uri}'):
                result_tuple = get_ns_and_name_from_uri(uri)
                self.assertEqual(expected_tuple, result_tuple)

    def test_get_class_directory_from_ns(self):
        testset = {
            'abstracten': 'Classes/Abstracten',
            'implementatieelement': 'Classes/ImplementatieElement',
            'installatie': 'Classes/Installatie',
            'levenscyclus': 'Classes/Levenscyclus',
            'onderdeel': 'Classes/Onderdeel',
            'proefenmeting': 'Classes/ProefEnMeting'
        }

        for ns, class_dir in testset.items():
            with self.subTest(f'get_class_directory_from {ns}'):
                result_class_dir = get_class_directory_from_ns(ns)
                self.assertEqual(class_dir, result_class_dir)

        with self.subTest('bad value'):
            with self.assertRaises(ValueError):
                get_class_directory_from_ns('bad_value')
