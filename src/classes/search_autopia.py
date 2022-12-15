from .search import Search
from .auto import Auto

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

class SearchAutopia(Search):
    def __init__(self, brand: str, model: str, from_year: int, until_year: int, quantity: int):
        Search.__init__(self, brand, model, from_year, until_year, quantity)
        self.__site = f"https://www.autopia.pe/resultados?marca={self._brand}&modelo={self._model}&ano-min={self._from_year}&ano-max={self._until_year}"
        self.__driver = None
        self.autos = []

    def _filter(self):
        options = Options()
        #options.add_argument('--headless')
        options.add_argument("--window-size=1920,1080")
        self.__driver = webdriver.Chrome(service=Service(self._path), options=options)
        #self.__driver = webdriver.Chrome(self._path)
        self.__driver.get(self.__site)
        #self.__driver.maximize_window()

    def get_autos(self):
        print(self.__site)
        container = self.__driver.find_element(By.XPATH, value='//div[@class="search-results"]')
        cars = container.find_elements(By.XPATH, value='//div[@class="car-card"]')

        for car in cars:
            try:
                url = car.find_element(By.XPATH, value='./a')
                url = url.get_attribute('href')
                price = car.find_element(By.XPATH, value='./a/div/div/p').text
                year = price
                price = price.split()[0]
                price = price.replace('$', '')
                price = price.replace(',', '')
                price = int(price)
                cant = len(year)
                year = year[-4:cant]
                auto = Auto(self._brand,self._model,year,price,url)
                self.autos.append(auto)
            except:
                pass
        self.autos.sort(key=lambda p: p.get_price())
        fin = len(self.autos) + 1
        del self.autos[self._quantity:fin]

        return self.autos
