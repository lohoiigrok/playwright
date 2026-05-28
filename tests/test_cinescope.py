import pytest
import allure
from page_object_models import CinescopeRegisterPage, CinescopeLoginPage
from generator import random_email, random_name, random_password

@allure.epic("Тестирование UI")
@allure.feature("Тестирование Страницы Login")
@pytest.mark.ui
class TestLoginPage:
    @pytest.mark.positive
    @allure.title("Проведение успешного входа в систему")
    def test_login_by_ui(self, page, registered_user):
        login_page = CinescopeLoginPage(page)
        login_page.open()
        login_page.login(registered_user.email, registered_user.password)

        login_page.assert_was_redirect_to_home_page()
        login_page.make_screenshot_and_attach_to_allure()
        login_page.assert_allert_was_pop_up()

    @pytest.mark.negative
    @allure.title("Проведение входа с неправильным паролем")
    def test_login_with_invalid_password(self, page, registered_user):
        login_page = CinescopeLoginPage(page)
        login_page.open()
        login_page.login(registered_user.email, "wrong_pssssword")

        login_page.assert_login_error_visible()
        login_page.make_screenshot_and_attach_to_allure()


@allure.epic("Тестирование UI")
@allure.feature("Тестирование Страницы Register")
@pytest.mark.ui
class TestRegisterPage:
    @pytest.mark.positive
    @allure.title("Проведение успешной регистрации")
    def test_register_by_ui(self, page):
        register_page = CinescopeRegisterPage(page)
        register_page.open()
        register_page.register(f"PlaywrightTest {random_name}", random_email, random_password,
                               random_password)

        register_page.assert_was_redirect_to_login_page()
        register_page.make_screenshot_and_attach_to_allure()
        register_page.assert_allert_was_pop_up()

    @pytest.mark.negative
    @allure.title("Проведение регистрации с неправильным email")
    def test_register_with_invalid_email(self, page):
        register_page = CinescopeRegisterPage(page)
        register_page.open()
        register_page.register(
            "PlaywrightTest User",
            "abc",
            "qwerty123",
            "qwerty123"
        )

        register_page.assert_email_error_visible()
        register_page.make_screenshot_and_attach_to_allure()

    @pytest.mark.negative
    @allure.title("Проведение регистрации с несовпадающим паролем")
    def test_register_with_password_mismatch(self, page):
        register_page = CinescopeRegisterPage(page)
        register_page.open()
        register_page.register(
            "PlaywrightTest User",
            "test123@email.qa",
            "wertt223",
            "werty4567"
        )

        register_page.assert_password_error_visible()
        register_page.make_screenshot_and_attach_to_allure()