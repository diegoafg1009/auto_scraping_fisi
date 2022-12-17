import uuid
from .config_file import ConfigFile

class Auto:

    def __init__(self, brand: str, model: str, year: int, price: int, url: str):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__price = price
        self.__url = url

    def get_year(self):
        return self.__year

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    def get_url(self):
        return self.__url

    def add_favorite(self, user_id):
        id = str(uuid.uuid1())
        brand = str(self.__brand)
        model = str(self.__model)
        year = self.__year
        price = self.__price
        url = str(self.__url)
        new_favorite = {"id": id, "brand": brand, "model": model, "year": year, "price": price, "url": url}
        ConfigFile.save_favorite(new_favorite, user_id)



