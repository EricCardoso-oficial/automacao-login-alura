import selenium
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import (NoSuchDriverException,
SessionNotCreatedException, WebDriverException, TimeoutException, 
NoSuchElementException, ElementClickInterceptedException, TimeoutException)

TEMPO = 15
URL_ALURA = ("https://www.alura.com.br/"
            "?srsltid=AfmBOopdwX-Amu5IjR_8320Mvwi4XhY"
            "_KZQ6Xt2h7Lu2wThXpQAQjVPr")

class LoginAlura:
    def __init__(self, email: str, senha: str):
        self.email = email
        self.senha = senha
    
    def configuracao_driver(self):
        try:
            self.opcoes = ChromeOptions()
            self.servico = Service(ChromeDriverManager().install())
            self.navegador = webdriver.Chrome(
                options=self.opcoes,
                service=self.servico)
        except (NoSuchDriverException, SessionNotCreatedException):
            print(
            'Erro: Driver não encontrado ou versão incompativél com o chrome')
            raise