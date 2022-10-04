class Auto:

    def __init__(self, name: str, year: int, brand: str, model: str, price: int, url: str):
        self.__name = name
        self.__year = year  # private
        self.__brand = brand
        self.__model = model
        self.__price = price
        self.__url = url

    def get_name(self):
        return self.__name

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
