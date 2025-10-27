from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class BasePage:
    """
    Clase base para todos los Page Objects. Contiene métodos genéricos
    de interacción con Selenium y la inicialización de esperas explícitas.
    """
    def __init__(self, driver: WebDriver):
        self.driver = driver

        self.timeout = 20 
        self.wait = WebDriverWait(self.driver, self.timeout)

    def find_element(self, locator: tuple) -> WebElement:
        """
        Espera hasta que el elemento esté presente en el DOM y lo devuelve.
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_and_click(self, locator: tuple):
        """
        Espera hasta que el elemento sea clickeable (visible y habilitado) y hace clic.
        Este es el método RECOMENDADO para clics.
        """
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    def wait_and_enter_text(self, locator: tuple, text: str):
        """
        Espera hasta que el elemento sea visible para ingresar texto.
        """
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)