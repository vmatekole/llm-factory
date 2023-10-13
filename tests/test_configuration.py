import unittest

from llm_maker.base_llm import Configuration


class TestConfiguration(unittest.TestCase):
    def test_initialization(self):
        config: Configuration = Configuration(option1=42, model_size='base')

        self.assertEqual(config.option1, 42)
        self.assertEqual(config.model_size, 'base')

    def test_readonly_attribute(self):
        config: Configuration = Configuration(option1=42, model_size='small')

        with self.assertRaises(AttributeError):
            config.option3 = 'new_value'

    def test_repr_method(self):
        config: Configuration = Configuration(option1=42, model_size='medium')

        expected_repr = 'option1: 42 model_size: medium '
        self.assertEqual(repr(config), expected_repr)

    def test_readonly_attribute_after_initialization(self):
        config: Configuration = Configuration(option1=42, model_size='large')

        with self.assertRaises(expected_exception=AttributeError):
            config.model_size = 'small'
