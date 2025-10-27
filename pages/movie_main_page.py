from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class MovieMainPage(BasePage):
    
    SEARCH_INPUT_LOCATOR = (By.NAME, "q") 
        
    def search_movie(self, name):
        """Escribe el nombre de la película y presiona ENTER."""

        self.wait_and_enter_text(self.SEARCH_INPUT_LOCATOR, name)

        time.sleep(10)
        
        self.find_element(self.SEARCH_INPUT_LOCATOR).send_keys(Keys.ENTER)