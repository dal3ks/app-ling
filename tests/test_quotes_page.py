from playwright.sync_api import Page, expect

def test_has_header(page: Page):
    page.goto("http://127.0.0.1:5001/quotes")

    h1 = page.locator("h1")

    expect(h1).to_have_text("Quotes")

def test_returns_list_of_reading_quotes(page: Page):
    page.goto("http://127.0.0.1:5001/quotes")

    quotes = page.locator('li')
    expected_quotes = ['Books are a uniquely portable magic by Stephen King',
    'Today a reader, tomorrow a leader by Margaret Fuller',
    'A good book is an event in my life. by Stendhal',
    'Reading is a discount ticket to everywhere by Mary Schmich']

    actual_quotes = quotes.all_inner_texts()
    assert actual_quotes == expected_quotes