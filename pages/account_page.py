import allure

from data import TU
from locators.account_page_locators import TLAP
from locators.home_page_locators import TLHP
from pages.home_page import HomePage


class AccountPage(HomePage):

    @allure.step('метод открывает страницу "Восстановление пароля"')
    def open_page_restore_password(self):
        # дождаться закрытия модального окна
        self.close_modal_if_present()
        # открыть страницу "Вход"
        self.clic_on_element(TLHP.LOCATOR_PERSONAL_ACCOUNT)
        # открыть страницу "Восстановление пароля"
        self.clic_on_element(TLAP.LOCATOR_RECOVER_PASSWORD)


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

