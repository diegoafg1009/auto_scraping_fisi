from classes import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = "C:\Program Files (x86)\chromedriver.exe"
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service=Service(PATH), options=options)
# # driver = webdriver.Chrome(service=Service(PATH))
driver.get("https://neoauto.com/")

driver.find_element(By.XPATH, value="/html/body/section[2]/div/div[2]/form/div/div[1]/div/div[3]/label").click()

print(driver.title)



