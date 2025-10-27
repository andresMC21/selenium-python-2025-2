from selenium import webdriver

def before_scenario(context, scenario):
    """
    Esta función se ejecuta antes de cada escenario de prueba.
    Inicializa el WebDriver y lo almacena en el contexto.
    """
    context.driver = webdriver.Chrome()  # o webdriver.Firefox()
    context.driver.maximize_window()

    if "bruno mars" in scenario.name.lower():
        context.driver.get("https://www.last.fm")
    
    elif "movie" in scenario.name.lower():
        context.driver.get("https://www.imdb.com")

def after_scenario(context, scenario):
    """
    Esta función se ejecuta después de cada escenario de prueba.
    Cierra el navegador para limpiar después de cada prueba.
    """
    context.driver.quit()
