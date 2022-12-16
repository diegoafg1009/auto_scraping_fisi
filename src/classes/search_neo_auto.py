from .auto import Auto
from .search import Search

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SearchNeoAuto(Search):

    def __init__(self, brand: str, model: str, from_year: int, until_year: int, quantity: int):
        Search.__init__(self, brand, model, from_year, until_year, quantity)
        self.__site = "https://neoauto.com/"
        self.__driver = None
        self.autos = []

    def __filter_by_brand(self):
        self._brand = self._brand.lower()
        brand = WebDriverWait(self.__driver, 5).until(
            ec.presence_of_element_located(
                (By.XPATH, f"//select[@class = 'select_brand']/option[@value='{self._brand.replace(' ','-')}']")))
        brand.click()

    def __filter_by_model(self):
        self._model = self._model.lower()
        model = WebDriverWait(self.__driver, 5).until(
            ec.presence_of_element_located(
                (By.XPATH, f"//select[@class = 'select_model']//option[@value = '{self._model.replace(' ','-')}']")))
        model.click()

    def __filter_by_years(self):
        from_year = self.__driver.find_element(By.XPATH, value="//input[@id = 'anioDesde']")
        from_year.send_keys(self._from_year)
        until_year = self.__driver.find_element(By.XPATH, value="//input[@id = 'anioHasta']")
        until_year.send_keys(self._until_year)
        self.__driver.find_element(By.XPATH,
                                   value="//button[@class='btn btn_diagonal submit_search_advanced']").click()

    def _filter(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.__driver = webdriver.Chrome(service=Service(self._path), options=options)
        self.__driver.get(self.__site)
        self.__driver.find_element(By.XPATH, value="//label[@for = 'vehicleOthers']").click()
        try:
            self.__filter_by_brand()
        except:
            print("No se encontro la marca buscada en NeoAuto")
            return False
        else:
            try:
                self.__filter_by_model()
            except:
                print("No se encontro el modelo buscado en NeoAuto")
                return False
            else:
                self.__filter_by_years()

    def get_autos(self):
        if self._filter() is False:
            return None
        else:
            i = 0
            order_by = Select(self.__driver.find_element(By.XPATH, value="//select[@class='c-select__select']"))
            order_by.select_by_visible_text("Menor precio")
            container = self.__driver.find_element(By.XPATH,
                                                   value="//div[contains(@class, 's-results') and contains(@class, 'js-container')]")
            articles = container.find_elements(By.XPATH, value="//article[contains(@class, 'c-results-used')]")
            for article in articles:
                i += 1
                if i > self._quantity:
                    break
                else:
                    url = article.find_element(By.CSS_SELECTOR, value="a[class='c-results-use__link']")
                    url = url.get_attribute('href')
                    title = article.find_element(By.CSS_SELECTOR, value="div[class='c-results-used__header']")
                    title = title.text.rsplit(" ", 1)
                    year = int(title[1])
                    price = article.find_element(By.CSS_SELECTOR, value="strong[class='c-results-used__price--black']")
                    price = price.text
                    auto = Auto(self._brand, self._model, year, price, url)
                    self.autos.append(auto)
            return self.autos



