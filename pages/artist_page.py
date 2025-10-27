from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ArtistPage(BasePage):
    """
    Page Object para la interacción en Last.fm: búsqueda y página de artista.
    """

    SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'a[href="/search"]')
    SEARCH_INPUT_LOCATOR = (By.NAME, "q")
    FIRST_RESULT_LOCATOR = (By.CSS_SELECTOR, 'a.link-block-target')
    LATEST_RELEASE_DATE_LOCATOR = (By.CSS_SELECTOR, 'p.artist-header-featured-items-item-date')

    def __init__(self, driver):
        super().__init__(driver)

    def click_search_button(self):
        """Abre el campo de búsqueda haciendo clic en el icono de la lupa."""

        self.wait_and_click(self.SEARCH_BUTTON_LOCATOR)

    def search_artist(self, name):
        """Escribe el nombre del artista y presiona ENTER para iniciar la búsqueda."""

        self.wait_and_enter_text(self.SEARCH_INPUT_LOCATOR, name)
        
        self.find_element(self.SEARCH_INPUT_LOCATOR).send_keys(Keys.ENTER)

    def open_first_result(self):
        """Abre el primer resultado de la lista de búsqueda."""

        self.wait_and_click(self.FIRST_RESULT_LOCATOR)

    def get_latest_release_date(self):
        """Extrae la fecha del último lanzamiento en la página del artista."""
        try:
            date_element = self.find_element(self.LATEST_RELEASE_DATE_LOCATOR)
            return date_element.text.strip()
        except Exception as e:
            print(f"No se pudo encontrar la fecha del último lanzamiento. Error: {e}")
            return None