import re
from abc import ABC
from typing import Union

from injector import inject
from . import logger


class Configuration:
    def __init__(self, **kwargs: dict[str, Union[str, int]]):
        self._readonly = False

        for k, v in kwargs.items():
            setattr(self, k, v)
        self._readonly = True

    def __setattr__(self, __name: str, __v) -> None:
        if getattr(self, '_readonly', False):
            raise AttributeError('LLM configuration readonly')
        super().__setattr__(__name, __v)

    def __repr__(self) -> str:
        state = ''
        for k, v in self.__dict__.items():
            state += f'{k}: {v} '
        return state


class LLMModel(ABC):
    def __init__(self, config: Configuration) -> None:
        super().__init__()
        self._config = config
        logger.info(f'Init LLM of type:{type(self)} with:{config}')

    @property
    def provider(self) -> any:
        return self._provider


class LLMService:
    @inject
    def __init__(self, model: LLMModel):
        self._model = model

    @property
    def model(self) -> LLMModel:
        return self._model
