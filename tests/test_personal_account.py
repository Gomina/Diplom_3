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
        # открыть страницу "Восстановление пароля" и вернуть актуальный URL
        current_url = page.open_page_restore_password()
        # ожидаемый URL страницы "Восстановление пароля"
        expected_url = page.url_page_recover_password()
        assert current_url == expected_url


    @allure.title('Проверка ввода почты и клик по кнопке «Восстановить»')
    def test_password_recovery(self, driver):
        page = AccountPage(driver)
        test_email = TU.User_1["email"]
        # перейти на страницу с полем "Введите код из письма". Вернуть плейсхолдер поля "Введите код из письма"
        real_text = page.recover_password_new_password(email=test_email)
        expect_text = page.placeholder_field_enter_code_from_letter()
        assert real_text == expect_text


    @allure.title('Проверка активации поля "Пароль", при нажатии на кнопку показать/скрыть пароль')
    def test_select_frame_field_password(self, driver):
        page = AccountPage(driver)
        test_email = TU.User_1["email"]
        # перейти на страницу с полем "Введите код из письма".
        page.recover_password_new_password(email=test_email)
        # проверяем активность поля
        active_field = page.field_reset_password_is_active()
        assert  active_field


class TestPersonalAccount:

    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    def test_go_to_personal_account(self, driver):
        page = AccountPage(driver)
        # закрыть модальное окно
        page.close_modal_if_present()
        # кликнуть кнопку "Личный кабинет", вернуть актуальный URL
        current_url = page.open_page_login()
        # ожидаемый URL
        expected_url = page.URL_page_login()
        assert current_url == expected_url


    @allure.title('Проверка перехода по клику на «История заказов»')
    def test_go_to_order_history(self, driver, create_and_delete_user_with_data):
        page = AccountPage(driver)
        # загрузить страницу "Профиль"
        page.open_user_page(create_and_delete_user_with_data)
        # проверить, что открылась страница "История заказов"
        current_url = page.open_order_history_page()
        # ожидаемый URL
        expected_url = page.URL_rder_history_page()
        assert current_url == expected_url


    @allure.title('Проверка выхода из "Профиль" через кнопку "Выход"')
    def test_Logout(self, driver, create_and_delete_user_with_data):
        page = AccountPage(driver)
        # загрузить страницу "Профиль"
        page.open_user_page(create_and_delete_user_with_data)
        # выити из личного кабинета
        current_url = page.logout()
        # ожидаемый URL
        expected_url = page.URL_page_login()
        assert current_url == expected_url
