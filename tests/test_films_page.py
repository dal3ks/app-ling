from playwright.sync_api import Page, expect
from database_connection import DatabaseConnection

def test_has_header(page: Page):
    page.goto("http://127.0.0.1:5001/films")
    h1 = page.locator("h1")
    expect(h1).to_have_text("My Films")

def test_film_list_contains_all_films(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/films.sql")
    page.goto("http://127.0.0.1:5001/films")
    films = page.locator('li')
    expected_films = [
        'The Shawshank Redemption (Drama, 1994)',
        'The Dark Knight (Action, 2008)',
        'Lord of the Rings: The Fellowship of the Ring (Fantasy, 2001)',
        'The Matrix (Sci-fi, 1999)',
        'One Flew over the Cuckoos Nest (Dark Comedy, 1975)'
    ]
    actual_films = films.all_inner_texts()
    assert actual_films == expected_films

def test_create_new_film(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/films.sql")
    page.goto("http://127.0.0.1:5001/films")
    page.get_by_placeholder("Title").fill("Parasite")
    page.get_by_placeholder("Genre").fill("Thriller")
    page.get_by_placeholder("Release Date").fill("2019")
    page.get_by_role("button", name="Submit").click()
    films = page.locator('li')
    print(films)
    new_film = films.all_inner_texts()[-1]
    print(new_film)
    assert new_film == "Parasite (Thriller, 2019)"