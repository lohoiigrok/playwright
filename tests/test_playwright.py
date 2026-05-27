import time
from playwright.sync_api import sync_playwright

class GooglePage:
    def __init__(self, page):
        self.page = page
        self.url = "https://www.google.com/"

        self.search_input = 'textarea[name="q"]'
        self.search_button = 'input[value="Поиск в Google"]'
        self.lucky_button = 'input[value="Мне повезет"]'

    def open(self):
        """Открывает страницу Google."""
        self.page.goto(self.url)

    def enter_search_query(self, query):
        """Вводит текст в строку поиска."""
        self.page.fill(self.search_input, query)

    def click_search_button(self):
        """Нажимает кнопку 'Поиск Google'."""
        self.search_button.click()

    def click_lucky_button(self):
        """Нажимает кнопку 'Мне повезет'."""
        self.page.click(self.lucky_button)

def test_page_object():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        google_page = GooglePage(page)

        google_page.open()

        google_page.enter_search_query("Аниме")

        google_page.enter_search_query("Вакансии?")

        google_page.enter_search_query("Page Object что это?")

        google_page.click_search_button()
        time.sleep(10)

        page.wait_for_selector("h3")

        browser.close()