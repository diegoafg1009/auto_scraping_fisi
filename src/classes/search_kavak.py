from .auto import Auto

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

class SearchKavak():

    def __init__(self, brand: str, model: str, quantity: int):
        self._brand = brand.lower()
        self._model = model.capitalize()
        self._quantity = quantity
        self.__path = "C:\Program Files (x86)\chromedriver.exe"
        self.__site = "https://www.kavak.com/pe/carros-usados"
        self.__driver = None
        self.autos = []

    def __filter(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--disable-gpu')
        self.__driver = webdriver.Chrome(service=Service(self.__path), options=options)
        self.__driver.get(self.__site)
        time.sleep(10)

        car_searched = (self._brand + " " + self._model).lower()
        search_box = self.__driver.find_element(By.ID, "input-search-catalogue")
        search_box.send_keys(car_searched)

        wait = WebDriverWait(self.__driver, 15)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@data-cy='btn-input-search-main']"))).click()
        wait.until(ec.element_to_be_clickable((By.XPATH, "//span[@class='select-value catalogue']"))).click()
        wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@aria-label='lowerPrice']"))).click()
        time.sleep(5)

    def __get_url(self):
        elements_with_urls = self.__driver.find_elements(
            By.XPATH, value="//div[@class='col-sm-6 col-car col-xl-4']//app-card-car//a[@class='card-inner']")
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
        self.__filter()
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
                print("Solo hay ", len(link_list), " autos disponibles")
                break
        return self.autos

    @classmethod
    def input_attributes(cls):
        brand = input("Marca: ")
        model = input("Modelo: ")
        quantity = int(input("Cantidad de resultados: "))
        return cls(brand, model, quantity)