from behave import given, when, then
from pages.artist_page import ArtistPage 

@given("the user is on the main page")
def step_impl(context):
    """Inicializa el Page Object y asegura que estamos listos para empezar."""
    context.page = ArtistPage(context.driver)

@when("he clicks the search button")
def step_impl(context):
    """Hace clic en la lupa para abrir el campo de búsqueda."""
    context.page.click_search_button()

@when('the user types the artist name "{artist_name}" and searches')
def step_impl(context, artist_name):
    """Escribe el nombre del artista y presiona ENTER para buscar."""

    context.page.search_artist(artist_name)

@when("opens the first result")
def step_impl(context):
    """Abre el primer resultado de la lista de búsqueda."""
    context.page.open_first_result()

@then('the user should be redirected to "{expectedUrl}" page')
def step_impl(context, expectedUrl):
    """Verifica que la página del artista ha cargado correctamente."""
    expected_name = expectedUrl
    
    page_content = context.driver.title + context.driver.current_url.lower()
    
    assert expected_name in page_content, \
           f"Expected to be on '{expected_name}' page, but Title/URL do not match: {context.driver.title} - {context.driver.current_url}"

@then('his latest release date must be "{expected_date}"')
def step_impl(context, expected_date):
    """Verifica que la fecha del último lanzamiento coincide con el valor esperado."""

    latest_release = context.page.get_latest_release_date() 
    
    assert latest_release == expected_date, \
           f"Date mismatch. Expected: '{expected_date}', but found: '{latest_release}'"