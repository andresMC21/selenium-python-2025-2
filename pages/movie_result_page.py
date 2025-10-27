# En pages/movie_page.py (asumiendo que hereda de BasePage)
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MovieResultPage(BasePage):
    
    FIRST_RESULT_LOCATOR = (By.CSS_SELECTOR, 'a.ipc-metadata-list-summary-item__t')

    def open_first_result(self):
        """Abre el primer resultado de la lista de búsqueda."""

        self.wait_and_click(self.FIRST_RESULT_LOCATOR)