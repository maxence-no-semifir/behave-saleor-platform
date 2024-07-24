import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Sealor:
    def __init__(self):
        self.service = Service(ChromeDriverManager().install())
        self.options = Options()
        
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--incognito')
        
        self.driver = webdriver.Chrome(service= self.service, options= self.options)
        self.wait = WebDriverWait(self.driver,10)
        
    def open_website(self,url):
        print(f'Opening website : {url}')

        self.driver.get(url)
        
    def click_button(self, by, value):
        try:
            print(f"Clicking button : {by} {value}")
            button = self.wait.until(EC.element_to_be_clickable((by,value)))
            button.click()
        except Exception as e :             
            print(f"An error occurred while trying to click the button: {e}")

    def enter_text(self, by, value, text):
        try:
            print(f"Entering text '{text}' in element: {by} {value}")
            input_field = self.wait.until(EC.visibility_of_element_located((by,value)))
            input_field.send_keys(text)
        except Exception as e:
            print(f"An error occurred while trying to enter text: {e}")
                     
                     
    def login(self, username, password):
        try:
            self.open_website("http://localhost:9000/dashboard/")
            # self.click_button(By.XPATH, '//*[@id="macaw-ui-root"]/div/div[1]/div/form/div/div[1]/div/input')  # Accepter les cookies
            self.enter_text(By.XPATH, '//*[@id="macaw-ui-root"]/div/div[1]/div/form/div/div[1]/div/input', username)  # Entrer l'email
            self.enter_text(By.XPATH, '//*[@id="macaw-ui-root"]/div/div[1]/div/form/div/div[3]/div/div/input', password)  # Entrer le mot de passe
            self.click_button(By.XPATH, '//*[@id="macaw-ui-root"]/div/div[1]/div/form/div/div[4]/button/span')  # Se connecter
            print("Connexion rÃ©ussie")
        except Exception as e:
            print(f"Erreur lors de la connexion: {e}")
            # self.save_screenshot("screenshort/error.png")
            
    
    def save_screenshot(self, file_path):
            try:
                # Vérifier si le dossier existe, sinon le créer
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                self.driver.save_screenshot(file_path)
                print(f"Capture d'écran enregistrée : {file_path}")
            except Exception as e:
                print(f"Erreur lors de la capture d'écran : {e}")