from langchain.llms.openai import OpenAI
from langchain.llms.gpt4all import GPT4All
from llm_maker.base_llm import Configuration, LLMModel
from injector import Module, provider, singleton

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from . import logger


class OpenAIModel(LLMModel):
    def __init__(self, model_name: str, config: Configuration) -> None:
        super().__init__(model_name)
        self._config = config
        self._provider = OpenAI(model_name, temperature=config.temperature)


class GPT4AllModel(LLMModel):
    def __init__(self, config: Configuration) -> None:
        super().__init__(config)
        self._config: Configuration = config

        callbacks = [StreamingStdOutCallbackHandler()]
        logger.error(f'CONFIG: {config}')
        self._provider: GPT4All = GPT4All(
            model=config.model_filepath, callbacks=callbacks, verbose=True
        )


class LLMFactory(Module):

    models = {'OPENAI': OpenAIModel, 'GPT4ALL': GPT4AllModel}

    def __init__(self) -> None:
        super().__init__()

    @provider
    @singleton
    def provide_model(self, config: Configuration) -> LLMModel:
        return LLMFactory.models[config.provider.upper()](config=config)
