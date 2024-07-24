from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from browser_actions import Sealor

def before_all(context):
    context.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    print("Initialisation du WebDriver")
    context.browser = Sealor()
    print("WebDriver initialisé avec succès")
    

def after_all(context):
    context.browser.quit()
