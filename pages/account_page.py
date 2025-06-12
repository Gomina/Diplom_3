import allure

from data import TD
from locators.account_page_locators import TLAP
from locators.home_page_locators import TLHP
from pages.home_page import HomePage
from urls import TestUrl


class AccountPage(HomePage):

    @allure.step('метод открывает страницу "Восстановление пароля"')
    def open_page_restore_password(self):
        # дождаться закрытия модального окна
        self.close_modal_if_present()
        # открыть страницу "Вход"
        self.clic_on_element(TLHP.LOCATOR_PERSONAL_ACCOUNT)
        # открыть страницу "Восстановление пароля"
        self.clic_on_element(TLAP.LOCATOR_RECOVER_PASSWORD)
        return self.driver.current_url


    @allure.step('метод переходить на стадию ввод кода из письма. Страница "Восстановление пароля"')
    def recover_password_new_password(self, email: str):
        # открыть страницу "Восстановление пароля"
        self.open_page_restore_password()
        # кликнуть на поле "Email"
        self.clic_on_element(TLAP.LOCATOR_FIELD_EMAIL)
        # вставить email
        self.set_text_to_element(TLAP.LOCATOR_FIELD_EMAIL, email)
        # кликнуть на кнопку "Восстановить"
        self.clic_on_element(TLAP.LOCATOR_BUTTON_RECOVER)
        return self.get_text_from_element(TLAP.LOCATOR_FIELD_CODE_FROM_LETTER)


    @allure.step('метод переходит на страницу "Профиль')
    def open_user_page(self, user_data: dict):
        # закрыть модальное окно
        self.close_modal_if_present()
        # кликнуть кнопку «Личный кабинет»
        self.clic_on_element(TLHP.LOCATOR_PERSONAL_ACCOUNT)
        # кликнуть поле "Email"
        self.clic_on_element(TLAP.LOCATOR_FIELD_EMAIL_LOGIN)
        # вставить email
        self.set_text_to_element(TLAP.LOCATOR_FIELD_EMAIL_LOGIN, user_data["email"])
        # кликнуть поле "Пароль"
        self.clic_on_element(TLAP.LOCATOR_FIELD_PASSWORD_LOGIN)
        # вставить пароль
        self.set_text_to_element(TLAP.LOCATOR_FIELD_PASSWORD_LOGIN, user_data["password"])
        # кликнуть кнопку "Войти"
        self.clic_on_element(TLAP.LOCATOR_BUTTON_LOGIN)
        # закрыть модальное окно
        self.close_modal_if_present()
        # кликнуть кнопку «Личный кабинет»
        self.clic_on_element(TLHP.LOCATOR_PERSONAL_ACCOUNT)


    @allure.step('метод возвращает ожидаемый URL страницы "Восстановление пароля"')
    def url_page_recover_password(self):
        return TestUrl.URL_PAGE_RECOVER_PASSWORD

    @allure.step('метод передает ожидаемый плейсхолдер поля "Введите код из письма"')
    def placeholder_field_enter_code_from_letter(self):
        return TD.FIELD_CODE_FROM_LETTER

    @allure.step('метод проверяет, что при нажатии на "глаз" поле становиться активным')
    def field_reset_password_is_active(self):
        self.close_modal_if_present()
        self.clic_on_element(TLAP.LOCATOR_SHOW_HIDE_PASSWORD)
        field_container = self.find_element_with_wait(TLAP.LOCATOR_INPUT_FIELD_BORDER)
        return "input_status_active" in field_container.get_attribute("class")

    @allure.step('метод проверяет, переход на страницу "Вход" по клику на кнопку "Личный кабинет"')
    def open_page_login(self):
        self.clic_on_element(TLHP.LOCATOR_PERSONAL_ACCOUNT)
        return self.driver.current_url

    @allure.step('метод возвращает ожидаемый URL страницы "Вход"')
    def URL_page_login(self):
        return TestUrl.URL_PAGE_LOGIN

    @allure.step('метод переходит на страницу "История заказов" и возвращает актуальный URL')
    def open_order_history_page(self):
        self.clic_on_element(TLAP.LOCATOR_HISTORY_ORDER)
        return self.driver.current_url

    @allure.step('метод возвращает ожидаемый URL страницы "История заказов"')
    def URL_rder_history_page(self):
        return TestUrl.URL_HISTORY_ORDER

    @allure.step('метод выходит из аккаунта и возвращает актуальный URL')
    def logout(self):
        # кликнуть кнопку «Выход»
        self.clic_on_element(TLAP.LOCATOR_BUTTON_LOGOUT)
        # дождаться чтобы URL "Вход" прогрузился
        self.loading_page_with_url(TestUrl.URL_PAGE_LOGIN)
        return self.driver.current_url

