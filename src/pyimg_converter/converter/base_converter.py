from __future__ import annotations

from abc import ABC, abstractmethod


# The `BaseConverter` class is an abstract base class that defines a method `convert_from_path` which
# must be implemented by its subclasses.
class BaseConverter(ABC):
    @abstractmethod
    def convert_from_path(self, input_path: str):
        raise NotImplementedError
