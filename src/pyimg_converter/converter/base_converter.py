from abc import ABC, abstractmethod


class BaseConverter(ABC):
    @abstractmethod
    def convert_from_path(self, input_path: str):
        raise NotImplementedError