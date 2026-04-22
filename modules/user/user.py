from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#importa dia,mes e ano de um select
from selenium.webdriver.support.ui import Select

#find_element procura um elemento sem espera,busca direta
# ec _element_to_be_clickable espera por exemplo,se o elemento foi renderizado,util para evitar craches  ou automação quebre 
# instancia de classes é self
# web driver wait é usado para aguardar uma condição ser verdadeira
class User:

    # configurando o webdriver
    def __init__(self):
        options = Options()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)

        self.url = "https://automationexercise.com/"
        self.driver.get(self.url)

    def create_driver(self):
        botao_login = self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                '#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(4) > a'
            ))
        )
        botao_login.click()

    def clicar_digitar_nome(self):
        campo = self.wait.until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                '#form input[type="text"]'
            ))
        )
        campo.clear()
        campo.send_keys("George lucas silva leitao")

    def clicar_email(self):
        campo_email = self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                '#form > div > div > div:nth-child(3) > div > form > input[type=email]:nth-child(3)'
            ))
        )
        campo_email.click()
        campo_email.send_keys("georgelucas.leitao20004@gmail.com")

    def botao_cadastro(self):
        campo_botao_cadastro = self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                '#form > div > div > div:nth-child(3) > div > form > button'
            ))
        )
        campo_botao_cadastro.click()

    def clicar_radio(self):
        radio_clique = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#id_gender1"))
        )
        radio_clique.click()

    def clicar_senha(self):
        criar_senha = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#password"))
        )
        criar_senha.click()
        criar_senha.send_keys("1q^gb&NkJ8!8")

    def selecionar_data_aniversario(self):
        elemento_dia = Select(self.driver.find_element(By.CSS_SELECTOR, "#days"))
        elemento_mes = Select(self.driver.find_element(By.CSS_SELECTOR, "#months"))
        elemento_ano = Select(self.driver.find_element(By.CSS_SELECTOR, "#years"))
        elemento_dia.select_by_value("4")
        elemento_mes.select_by_value("1")
        elemento_ano.select_by_value("2004")


    def primeiro_nome(self):
      primeiro_nome = self.wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#first_name"))
    )
    
    def segundo_nome(self):
      self.segundo_nome = self.wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "##last_name"))
    )
    def empresa_companhia(self):
        self.empresa_companhia = self.wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#company"))
    )
    empresa_companhia.send_keys("fpf tech")
    
# deve ser de forma linear
if __name__ == "__main__":  
    user = User()
    user.create_driver()
    user.clicar_digitar_nome()
    user.clicar_email()
    user.botao_cadastro()
    user.clicar_radio()
    user.clicar_senha()
    user.selecionar_data_aniversario()
    user.empresa_companhia()

    input("Pressione ENTER para encerrar")