from abc import ABC
from abc import abstractmethod
from pathlib import Path


class Search(ABC):
    def __init__(self, brand: str, model: str, from_year: int, until_year: int, quantity: int):
        self._path = self.get_path()
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

    def get_path(self):
        driver_path = Path().absolute().parent
        driver_path = Path(driver_path, "driver_path.txt")
        with open(driver_path, 'r') as file:
            path = file.readline()
        return path
