from behave import given, when, then
from pages.movie_main_page import MovieMainPage 
from pages.movie_result_page import MovieResultPage 
from pages.movie_description_page import MovieDescriptionPage 

@given("the user is on the main movie page")
def step_impl(context):
    """
    Inicializa la clase MoviePage y maneja la navegación/cookies.
    Asume que la URL ya se cargó en environment.py.
    """
    context.page = MovieMainPage(context.driver)


@when('the user searches for the movie "{movie_name}"')
def step_impl(context, movie_name):
    """Escribe el nombre de la película y presiona ENTER."""
    context.page.search_movie(movie_name)


@when("opens the first search result")
def step_impl(context):
    context.page = MovieResultPage(context.driver)
    """Abre el primer resultado de la lista de búsqueda."""
    context.page.open_first_result()

@then('the user should be redirected to the "{expected_title}" movie page')
def step_impl(context, expected_title):
    context.page = MovieDescriptionPage(context.driver)
    """
    Verifica que el usuario ha sido redirigido a la página de detalles correcta.
    Comprueba que el título de la página (o la URL) contenga el nombre de la película.
    """
    page_content = context.driver.title.lower() + context.driver.current_url.lower()
    
    assert expected_title.lower() in page_content, \
           f"Redirection failed. Expected to find '{expected_title}' in Title or URL, but got: {context.driver.title} and {context.driver.current_url}"

@then('the movie title displayed must be "{expected_title}"')
def step_impl(context, expected_title):
    """Verifica que el título principal extraído de la página coincida con el valor esperado."""
    actual_title = context.page.get_movie_title()
    
    assert actual_title.strip() == expected_title, \
           f"Title mismatch. Expected: '{expected_title}', but found: '{actual_title}'"

@then('the movie rating must be "{expected_rating}"')
def step_impl(context, expected_rating):
    """Verifica que la calificación (rating) extraída coincida con el valor esperado."""
    actual_rating = context.page.get_movie_rating()
    
    assert actual_rating == expected_rating, \
           f"Rating mismatch. Expected: '{expected_rating}', but found: '{actual_rating}'"