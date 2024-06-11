from abc import ABC, abstractmethod

class IResponseModel(ABC):
    @abstractmethod
    def to_dict(self) -> dict:
        raise NotImplementedError("Subclasses must implement to_dict()")
