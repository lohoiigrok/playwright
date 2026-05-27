import pytest
import allure
import time
from playwright.sync_api import sync_playwright
from page_object_models import CinescopeRegisterPage, CinescopeLoginPage
from generator import random_email, random_name, random_password

@allure.epic("Тестирование UI")
@allure.feature("Тестирование Страницы Login")
@pytest.mark.ui
class TestLoginPage:
    @allure.title("Проведение успешного входа в систему")
    def test_login_by_ui(self, registered_user):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(
                headless=False)
            page = browser.new_page()
            login_page = CinescopeLoginPage(page)

            login_page.open()
            login_page.login(registered_user.email, registered_user.password)

            login_page.assert_was_redirect_to_home_page()
            login_page.make_screenshot_and_attach_to_allure()
            login_page.assert_allert_was_pop_up()

            time.sleep(5)
            browser.close()


@allure.epic("Тестирование UI")
@allure.feature("Тестирование Страницы Register")
@pytest.mark.ui
class TestRegisterPage:
    @allure.title("Проведение успешной регистрации")
    def test_register_by_ui(self):
        with sync_playwright() as playwright:

            browser = playwright.chromium.launch(
                headless=False)
            page = browser.new_page()

            register_page = CinescopeRegisterPage(page)
            register_page.open()
            register_page.register(f"PlaywrightTest {random_name}", random_email, random_password,
                                   random_password)

            register_page.assert_was_redirect_to_login_page()
            register_page.make_screenshot_and_attach_to_allure()
            register_page.assert_allert_was_pop_up()

            time.sleep(5)
            browser.close()

