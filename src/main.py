import os
import pyautogui as pag
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from utils import esperar_elemento
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import (NoSuchDriverException,
SessionNotCreatedException, WebDriverException, TimeoutException, 
NoSuchElementException, ElementClickInterceptedException,
ElementNotInteractableException)

TEMPO = 20
URL_ALURA_LOGIN = ("https://cursos.alura.com.br/loginForm")

class LoginAlura:
    def __init__(self, email: str, senha: str):
        self.email = email
        self.senha = senha
    
    def configuracao_driver(self):
        try:
            # Configura as opções
            self.opcoes = ChromeOptions()
            
            # Configura o serviço
            self.servico = Service(ChromeDriverManager().install())
            
            # Configura o driver
            self.driver = webdriver.Chrome(
                options=self.opcoes,
                service=self.servico)
        
        except (NoSuchDriverException, SessionNotCreatedException):
            print(
            'Erro: Driver não encontrado ou versão incompativél com o chrome')
            raise

    def logar(self):
        # Acessar o Alura
        self.driver.get(URL_ALURA_LOGIN)
        
        # Maximizar a tela
        self.driver.maximize_window()
        sleep(10)

        try:
            # Procurar o botão de Logar com o Google
            self.botao_logar_google = esperar_elemento(
                driver=self.driver, 
                tempo=TEMPO, 
                chave=By.CLASS_NAME, 
                valor="button-secondary-blue"
            )
            
            # Clicar no botão
            self.botao_logar_google.click()
            sleep(8)

            # Procurar o campo para inserir o Gmail
            self.driver.switch_to.window(self.driver.window_handles[-1])
        
            self.campo_gmail = esperar_elemento(
                driver=self.driver,
                tempo=TEMPO,
                chave=By.ID,
                valor="identifierId"
            )

            # Carregar as variáveis de ambiente
            load_dotenv()
            
            # Pegar o Gmail do usuário
            gmail_usuario = os.getenv("GMAIL")
            
            # Inserir Gmail
            self.campo_gmail.send_keys(gmail_usuario)
            
            # Pressionar o Enter
            self.campo_gmail.send_keys(Keys.ENTER)
            sleep(8)

            # Procurar o campo para inserir a Senha
            self.campo_senha = esperar_elemento(
                driver=self.driver,
                tempo=TEMPO,
                chave=By.NAME,
                valor="Passwd"
            )

            # Pegar a senha do usuário
            senha_usuario = os.getenv("SENHA_GMAIL")
            
            # Inserir a senha
            self.campo_senha.send_keys(senha_usuario)
            
            # Pressionar Enter
            self.campo_senha.send_keys(Keys.ENTER)
            sleep(10)

            pag.press("Esc")
            sleep(8)

        except NoSuchElementException:
            print("Elemento não encontrado")
            raise
        
        except ElementNotInteractableException:
            print("O elemento não é interagível")
            raise
        
        except TimeoutException:
            print("O tempo esgotou antes da condição ser atendida")
            raise
