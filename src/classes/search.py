from abc import ABC
from abc import abstractmethod


class Search(ABC):
    def __init__(self, brand: str, model: str, from_year: int, until_year: int, quantity: int):
        self._path = "C:\Program Files (x86)\chromedriver.exe"
        self._brand = brand.lower()
        self._model = model.lower()
        self._from_year = from_year
        self._until_year = until_year
        self._quantity = quantity


    @abstractmethod
    def _filter(self):
        pass

    @abstractmethod
    def get_autos(self):
        pass
