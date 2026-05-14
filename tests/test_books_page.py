from playwright.sync_api import Page, expect
from database_connection import DatabaseConnection

def test_has_header(page: Page):
    page.goto("http://127.0.0.1:5001/books")

    h1 = page.locator("h1")

    expect(h1).to_have_text("My Books")

def test_book_list_contains_all_books(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")
    page.goto("http://127.0.0.1:5001/books")

    books = page.locator('li')

    expected_books = [
    'Misinterpretation by Ledia Xhoga',
    'Drive Your Plow Over the Bones of the Dead by Olga Tokarczuk',
    'Infinite Jest by David Foster Wallace',
    'Blazing World by Margaret Cavendish',
    'The Silmarillion by J R R Tolkien'
    ]
    # here's the neat part which saves you from iterating over the `li` elements
    actual_books = books.all_inner_texts()

    assert actual_books == expected_books
    #assert len(actual_books) >= 5

def test_create_new_book(page: Page):
    page.goto("http://127.0.0.1:5001/books")
    page.get_by_placeholder("Title").fill("Known and Strange Things")
    page.get_by_placeholder("Author").fill("Teju Cole")
    page.get_by_role("button", name="Submit").click()
    books = page.locator('li')
    new_book = books.all_inner_texts()[-1]
    assert new_book == "Known and Strange Things by Teju Cole"
