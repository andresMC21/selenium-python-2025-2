# En pages/movie_page.py (asumiendo que hereda de BasePage)
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MovieDescriptionPage(BasePage):
    
    MOVIE_TITLE_LOCATOR = (By.CSS_SELECTOR, '[data-testid="hero__primary-text"]') 
    MOVIE_RATING_LOCATOR = (By.CSS_SELECTOR, '.lbQcRY')

    def get_movie_title(self) -> str:
        """Extrae el título principal de la página de detalles de la película."""
        element = self.find_element(self.MOVIE_TITLE_LOCATOR)
        return element.text.strip()

    def get_movie_rating(self) -> str:
        """Extrae la calificación (rating) de la película."""
        element = self.find_element(self.MOVIE_RATING_LOCATOR)
        return element.text.strip()