import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

class User:
    def __init__(self):
        options = Options()
        options.add_experimental_option("detach", True)
        
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.url = "https://automationexercise.com/"
        self.driver.get(self.url)

    def ir_para_login_signup(self):
        botao_login = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Signup / Login')]"))
        )
        botao_login.click()

    def realizar_fluxo_usuario(self, nome, email, senha):
        self.ir_para_login_signup()
        
        campo_nome = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-qa="signup-name"]')))
        campo_email = self.driver.find_element(By.CSS_SELECTOR, 'input[data-qa="signup-email"]')
        
        campo_nome.send_keys(nome)
        campo_email.send_keys(email)
        
        botao_signup = self.driver.find_element(By.CSS_SELECTOR, 'button[data-qa="signup-button"]')
        botao_signup.click()
        
        try:
            erro_email = self.driver.find_element(By.XPATH, "//p[contains(text(), 'Email Address already exist!')]")
            if erro_email.is_displayed():
                print(f"O e-mail {email} já está cadastrado. Realizando login...")
                self.realizar_login(email, senha)
        except:
            print("Iniciando novo cadastro...")
            self.completar_cadastro(senha)

    def realizar_login(self, email, senha):
        campo_login_email = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-qa="login-email"]')))
        campo_login_senha = self.driver.find_element(By.CSS_SELECTOR, 'input[data-qa="login-password"]')
        
        campo_login_email.clear()
        campo_login_email.send_keys(email)
        campo_login_senha.clear()
        campo_login_senha.send_keys(senha)
        
        botao_login = self.driver.find_element(By.CSS_SELECTOR, 'button[data-qa="login-button"]')
        botao_login.click()
        print("Login realizado com sucesso!")

    def completar_cadastro(self, senha):
        self.wait.until(EC.element_to_be_clickable((By.ID, "id_gender1"))).click()
        self.driver.find_element(By.ID, "password").send_keys(senha)
        
        Select(self.driver.find_element(By.ID, "days")).select_by_value("4")
        Select(self.driver.find_element(By.ID, "months")).select_by_value("1")
        Select(self.driver.find_element(By.ID, "years")).select_by_value("2004")
        
        self.driver.find_element(By.ID, "first_name").send_keys("George Lucas")
        self.driver.find_element(By.ID, "last_name").send_keys("Silva Leitao")
        self.driver.find_element(By.ID, "company").send_keys("FPF Tech")
        self.driver.find_element(By.ID, "address1").send_keys("Rua Exemplo, 123")
        self.driver.find_element(By.ID, "country").send_keys("Canada")
        self.driver.find_element(By.ID, "state").send_keys("Amazonas")
        self.driver.find_element(By.ID, "city").send_keys("Manaus")
        self.driver.find_element(By.ID, "zipcode").send_keys("69000-000")
        self.driver.find_element(By.ID, "mobile_number").send_keys("92999999999")
        
        self.driver.find_element(By.CSS_SELECTOR, 'button[data-qa="create-account"]').click()
        print("Cadastro finalizado!")
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-qa="continue-button"]'))).click()

    def extrair_e_salvar_produtos(self):
        print("\nNavegando para a página de produtos...")
        self.driver.get("https://automationexercise.com/products")
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "features_items")))
        
        html_content = self.driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        itens_produtos = soup.find_all('div', class_='col-sm-4')
        
        dados_produtos = []
        
        for item in itens_produtos:
            info = item.find('div', class_='productinfo')
            if info:
                preco = info.find('h2').get_text(strip=True) if info.find('h2') else "N/A"
                nome = info.find('p').get_text(strip=True) if info.find('p') else "N/A"
                # Limpando o preço para deixar apenas números se possível
                preco_limpo = preco.replace("Rs. ", "").strip()
                dados_produtos.append({"Nome": nome, "Preço": preco_limpo})

        # Criando DataFrame e salvando em CSV
        df = pd.DataFrame(dados_produtos)
        df.to_csv("produtos_extraidos.csv", index=False, encoding='utf-8-sig')
        print(f"Sucesso! {len(df)} produtos salvos em 'produtos_extraidos.csv'.")

    def excluir_cadastro(self):
        print("\nIniciando processo de exclusão de conta...")
        try:
            botao_excluir = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Delete Account')]"))
            )
            botao_excluir.click()
            
            # Verificar se a conta foi realmente excluída (página de confirmação)
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h2[data-qa="account-deleted"]')))
            print("Conta excluída com sucesso!")
            
            # Clicar em Continue após exclusão
            self.driver.find_element(By.CSS_SELECTOR, 'a[data-qa="continue-button"]').click()
        except Exception as e:
            print(f"Erro ao tentar excluir a conta: {e}")

    def fechar(self):
        self.driver.quit()

if __name__ == "__main__":
    user_bot = User()
    try:
        NOME_USER = "George Lucas Silva Leitao"
        EMAIL_USER = "georgelucas.leitao20004@gmail.com"
        SENHA_USER = "1q^gb&NkJ8!8"
        
        # 1. Autenticação
        user_bot.realizar_fluxo_usuario(NOME_USER, EMAIL_USER, SENHA_USER)
        
        # 2. Extração e CSV
        user_bot.extrair_e_salvar_produtos()
        
        # 3. Exclusão de Conta
        user_bot.excluir_cadastro()
        
    except Exception as e:
        print(f"Ocorreu um erro no fluxo: {e}")
    finally:
        print("\nProcesso finalizado.")
        # user_bot.fechar()
