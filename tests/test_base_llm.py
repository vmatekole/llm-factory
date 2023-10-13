import unittest
from unittest.mock import Mock
from llm_maker.base_llm import LLMModel, LLMService, Configuration


class TestLLMModel(unittest.TestCase):
    def test_valid_initialization(self):
        config = Configuration(param1='value1', param2='value2')
        model = LLMModel(config)
        self.assertEqual(model._config, config)

    def test_invalid_initialization(self):
        with self.assertRaises(TypeError):
            model = LLMModel(None)

    def test_provider_property(self):
        config = Configuration(param1='value1', param2='value2')
        model = LLMModel(config)
        self.assertIsNone(model.provider)  # provider is not defined in the code


class TestLLMService(unittest.TestCase):
    def test_valid_initialization(self):
        model = Mock(spec=LLMModel)
        service = LLMService(model)
        self.assertEqual(service.model, model)

    def test_invalid_initialization(self):
        with self.assertRaises(TypeError):
            service = LLMService(None)
