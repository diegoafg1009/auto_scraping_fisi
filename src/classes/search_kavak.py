from .auto import Auto
from .search import Search

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

class SearchKavak(Search):

    def __init__(self, brand: str, model: str, from_year: int, until_year: int, quantity: int):
        Search.__init__(self, brand, model, from_year, until_year, quantity)
        self.__site = "https://www.kavak.com/pe/carros-usados"
        self.__driver = None
        self.autos = []

    def _filter(self):
        options = Options()
        #options.add_argument('--headless')
        options.add_argument("--window-size=1920,1080")
        self.__driver = webdriver.Chrome(service=Service(self.__path), options=options)
        self.__driver.get(self.__site)
        time.sleep(10)

        wait = WebDriverWait(self.__driver, 10)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//h3[@data-cy='btn-accordion-año']"))).click()
        self.__select_year()
        wait.until(ec.element_to_be_clickable((By.XPATH, "//h3[@data-cy='btn-accordion-año']"))).click()
        wait.until(ec.element_to_be_clickable((By.XPATH, "//h3[@data-cy='btn-accordion-marca-y-modelo']"))).click()
        wait.until(ec.element_to_be_clickable((By.XPATH, f"//img[@alt='{self._brand.capitalize()}']"))).click()
        wait.until(ec.element_to_be_clickable((By.XPATH, f"//button[@aria-label='Select {self._model.capitalize()}']"))).click()
        wait.until(ec.element_to_be_clickable((By.XPATH, "//span[@class='select-value catalogue']"))).click()
        wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@aria-label='lowerPrice']"))).click()
        time.sleep(3)

    def __get_url(self):
        elements_with_urls = self.__driver.find_elements(
            By.XPATH, value="//a[@class='card-inner']")
        urls = [url.get_attribute('href') for url in elements_with_urls]
        return urls

    def __get_price(self):
        elements_with_prices = self.__driver.find_elements(
            By.XPATH, value="//div[1][@class='payment-tax-wrapper']//span[@class='payment-total payment-highlight']")
        prices = [price.text for price in elements_with_prices]
        return prices

    def __get_year(self):
        elements_with_years = self.__driver.find_elements(
            By.XPATH, value="//p[@class='car-details']")
        years = [year.text for year in elements_with_years]
        return years

    def get_autos(self):
        i = 0
        self._filter()
        link_list = self.__get_url()
        price_list = self.__get_price()
        year_list = self.__get_year()

        while i < self._quantity:
            if i < len(link_list):
                link = link_list[i]
                price = price_list[i]
                year = year_list[i]
                auto = Auto(self._brand, self._model, year, price, link)
                self.autos.append(auto)
                i += 1
            else:
                break
        return self.autos

    def __select_year(self):
        conteinner = self.__driver.find_element(
            By.XPATH, value="//app-facet-attr")
        buttons = conteinner.find_elements(By.CSS_SELECTOR, value="button[class='no-focus btn-accent sc-kavak-button']")
        for button in buttons:
            if (int(button.text) >= self._from_year) and (int(button.text) <= self._until_year):
                button.click()