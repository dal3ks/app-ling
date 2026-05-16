from app import app
from database_connection import DatabaseConnection
from playwright.sync_api import Page

# Integration test for authentication:

def test_auth_integration():
    client = app.test_client()
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('test', '1234');")
    response = client.post('/sessions', data={
        'username': 'test',
        'password': '1234'})
    assert response.status_code == 302

# Playwright test for authentication:
def test_auth_playwright(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) VALUES ('test', '1234');")
    page.goto("http://127.0.0.1:5001/sessions/new")
    page.get_by_placeholder("username").fill("test")
    page.get_by_placeholder("password").fill("1234")
    page.get_by_role("button").click()
    assert page.url == "http://127.0.0.1:5001/books"


# Integration test for failed authentication:
def test_fails_authentication():
    client = app.test_client()
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('test', '1234');")

    response = client.post('/sessions', data={
        'username': 'wrong_username',
        'password': 'wrong_password'})
    assert response.location == "/sessions/new"


# Playwright test for failed authentication:
def test_fails_auth_playwright(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) VALUES ('test', '1234');")

    page.goto("http://127.0.0.1:5001/sessions/new")
    page.get_by_placeholder("username").fill("wrong_username")
    page.get_by_placeholder("password").fill("wrong_password")
    page.get_by_role("button").click()

    assert "/sessions" in page.url


# Playwright test for when unauthenticated user tries to create a book:

def tests_if_user_not_registered_tries_to_create_book(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) VALUES ('test', '1234');")

    page.goto("http://127.0.0.1:5001/books")
    page.get_by_placeholder("title").fill("Not a Book, first edition")
    page.get_by_placeholder("author").fill("Not a Person the Third")
    page.get_by_role("button").click()

    assert "/sessions/new" in page.url

