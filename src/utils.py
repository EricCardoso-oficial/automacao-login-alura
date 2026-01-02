from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def esperar_elemento(
        driver: webdriver, 
        tempo: int, 
        chave: By, 
        valor: str):
   
    return WebDriverWait(driver, tempo).until(
        EC.presence_of_element_located((chave, valor))
    )