import uuid
from .config_file import ConfigFile


class Favorite:
    def __init__(self, index: int):
        self.index = index


    @staticmethod
    def add_favorite(auto):
        id = str(uuid.uuid1())
        brand = str(auto.get_brand())
        model = str(auto.get_model())
        year = auto.get_year()
        price = auto.get_price()
        url = str(auto.get_url())
        new_favorite = {"id": id, "brand": brand, "model": model, "year": year, "price": price, "url": url}
        ConfigFile.save_favorite(new_favorite)






