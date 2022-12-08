import time
from .auto import Auto
from .search import Search
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SearchAutopia(Search):
    def __init__(self, brand: str, model: str, from_year: int, until_year: int, quantity: int):
        Search.__init__(self, brand, model, from_year, until_year, quantity)
        self._brand = brand.lower()
        self._model = model.capitalize()
        self._quantity = quantity
        self.__site = "https://www.autopia.pe/resultados"
        self.__driver = None
        self.autos = []

    def __filter(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--start-extensions')
        self.__driver = webdriver.Chrome(service=Service(self._path), options=options)
        self.__driver.get(self.__site)
        time.sleep(10)

        # Seleccionar Marca(Brand)
        WebDriverWait(self.__driver, 5) \
            .until(ec.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div/div/div[2]/div[1]/div[3]/h3'))) \
            .click()
        time.sleep(1)
        marca_link = self.__driver.find_elements(By.XPATH,
                                                 '/html/body/div[1]/div/div/div[2]/div[1]/div[3]/div/div/div/div[1]/div/ul/*')
        for e in marca_link:
            if e.text == self._brand:
                e.click()
                time.sleep(1)
                WebDriverWait(self.__driver, 5) \
                    .until(ec.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div[3]/div/div/div/div[2]/button[2]/p'))) \
                    .click()
                time.sleep(1)
                # Seleccionar Modelo(Model)
                WebDriverWait(self.__driver, 5) \
                    .until(ec.element_to_be_clickable((By.XPATH,
                                                       "/html/body/div[1]/div/div/div[2]/div[1]/div[4]/h3"))) \
                    .click()
                time.sleep(1)
                model_link = self.__driver.find_elements(By.XPATH,
                                                         '/html/body/div[1]/div/div/div[2]/div[1]/div[4]/div/div/div/div[1]/div/ul/*')
                for i in model_link:
                    if i.text == self._model:
                        i.click()
                        WebDriverWait(self.__driver, 5) \
                            .until(ec.element_to_be_clickable(
                            (
                            By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div[4]/div/div/div/div[2]/button[2]/p'))) \
                            .click()
                        # Seleccionar Año(Un intervalo)
                        WebDriverWait(self.__driver, 5) \
                            .until(ec.element_to_be_clickable(
                            (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div[6]/h3'))) \
                            .click()
                        time.sleep(2)
                        WebDriverWait(self.__driver, 5) \
                            .until(ec.element_to_be_clickable(
                            (By.XPATH,
                             '/html/body/div[1]/div/div/div[2]/div[1]/div[6]/div/div/div/div[1]/div/div[1]/input'))) \
                            .send_keys(self._from_year)
                        time.sleep(2)
                        WebDriverWait(self.__driver, 5) \
                            .until(ec.element_to_be_clickable(
                            (By.XPATH,
                             '/html/body/div[1]/div/div/div[2]/div[1]/div[6]/div/div/div/div[1]/div/div[2]/input'))) \
                            .send_keys(self._until_year)
                        time.sleep(2)
                        WebDriverWait(self.__driver, 5) \
                            .until(ec.element_to_be_clickable(
                            (
                            By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div[6]/div/div/div/div[2]/button[2]/p'))) \
                            .click()
                        time.sleep(2)
                        WebDriverWait(self.__driver, 5) \
                            .until(ec.element_to_be_clickable(
                            (By.XPATH, '/html/body/div[1]/div/div/div[3]'))) \

                        time.sleep(2)

                        self.__driver.quit()
