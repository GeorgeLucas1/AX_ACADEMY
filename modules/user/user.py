from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class User:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "https://automationexercise.com/"
        self.driver.get(self.url)

    def create_driver(self):
        self.driver.find_element(By.CSS_SELECTOR, '#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(4) > a').click()

#encontra o elemento
#preencher o elemento 
def  criar_usuario(self):
self.driver.find_element(  By.CSS_SELECTOR,'#form > div > div > div:nth-child(3) > div > form > input[type=text]:nth-child(2)'
).click()    




    
if __name__ == "__main__":
    user = User()
    user.create_driver()
    user.driver.find_element()