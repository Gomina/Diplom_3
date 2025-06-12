import pytest
import allure

from data import TD, TU
from locators.account_page_locators import TLAP
from locators.home_page_locators import TLHP
from pages.account_page import AccountPage
from urls import TestUrl


class TestPasswordRecovery:


    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_page_recover_password(self, driver):
        page = AccountPage(driver)
        page.open_page_restore_password()
        # проверить, что открылась страница "Восстановление пароля"
        current_url = driver.current_url
        expected_url = TestUrl.URL_PAGE_RECOVER_PASSWORD
        assert current_url == expected_url


    @allure.title('Проверка ввода почты и клик по кнопке «Восстановить»')
    def test_password_recovery(self, driver):
        page = AccountPage(driver)
        test_email = TU.User_1["email"]
        # перейти на страницу с полем "Введите код из письма"
        page.recover_password_new_password(email=test_email)
        real_text = page.get_text_from_element(TLAP.LOCATOR_FIELD_CODE_FROM_LETTER)
        expect_text = TD.FIELD_CODE_FROM_LETTER
        assert real_text == expect_text


    @allure.title('Проверка активации поля "Пароль", при нажатии на кнопку показать/скрыть пароль')
    def test_select_frame_field_password(self, driver):
        page = AccountPage(driver)
        test_email = TU.User_1["email"]
        # перейти на страницу с полем "Введите код из письма"
        page.recover_password_new_password(email=test_email)
        # нажать на кнопку "глаз"
        page.clic_on_element(TLAP.LOCATOR_SHOW_HIDE_PASSWORD)
        # найти поле
        field_container = page.find_element_with_wait(TLAP.LOCATOR_INPUT_FIELD_BORDER)
        # проверить статус
        assert "input_status_active" in field_container.get_attribute("class")


class TestPersonalAccount:

    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    def test_go_to_personal_account(self, driver):
        page = AccountPage(driver)
        # закрыть модальное окно
        page.close_modal_if_present()
        # кликнуть кнопку «Личный кабинет»
        page.clic_on_element(TLHP.LOCATOR_PERSONAL_ACCOUNT)
        # проверить, что открылась страница "Вход"
        current_url = driver.current_url
        expected_url = TestUrl.URL_PAGE_LOGIN
        assert current_url == expected_url


    @allure.title('Проверка перехода по клику на «История заказов»')
    def test_go_to_order_history(self, driver, create_and_delete_user_with_data):
        page = AccountPage(driver)
        # загрузить страницу "Профиль"
        page.open_user_page(create_and_delete_user_with_data)
        # кликнуть «История заказов»
        page.clic_on_element(TLAP.LOCATOR_HISTORY_ORDER)
        # проверить, что открылась страница "История заказов"
        current_url = driver.current_url
        expected_url = TestUrl.URL_HISTORY_ORDER
        assert current_url == expected_url


    @allure.title('Проверка выхода из "Профиль" через кнопку "Выход"')
    def test_Logout(self, driver, create_and_delete_user_with_data):
        page = AccountPage(driver)
        # загрузить страницу "Профиль"
        page.open_user_page(create_and_delete_user_with_data)
        # кликнуть кнопку «Выход»
        page.clic_on_element(TLAP.LOCATOR_BUTTON_LOGOUT)
        # дождаться чтобы URL "Вход" прогрузился
        page.loading_page_with_url(TestUrl.URL_PAGE_LOGIN)
        # проверить, что открылась страница "История заказов"
        current_url = driver.current_url
        expected_url = TestUrl.URL_PAGE_LOGIN
        assert current_url == expected_url
