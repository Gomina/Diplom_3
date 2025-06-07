import allure
import pytest

from data import TD
from locators.home_page_locators import TLHP
from pages.account_page import AccountPage
from pages.home_page import HomePage
from urls import TestUrl


class TestBasicFunctions:


    @allure.title('Проверка перехода по клику на «Конструктор»')
    def test_transition_to_constructor(self, driver):
        page = HomePage(driver)
        # закрыть модальное окно
        page.close_modal_if_present()
        # перейти на страницу "Вход"
        page.clic_on_element(TLHP.LOCATOR_PERSONAL_ACCOUNT)
        # кликнуть "Конструктор"
        page.clic_on_element(TLHP.LOCATOR_BUTTON_CONSTRUCTOR)
        # проверить, что открылась страница "Конструктор"
        current_url = driver.current_url
        expected_url = TestUrl.URL_PAGE_CONSTRUCTOR
        assert current_url == expected_url


    @allure.title('Проверка перехода по клику на  «Лента заказов»')
    def test_transition_to_order_feed(self, driver):
        page = HomePage(driver)
        # закрыть модальное окно
        page.close_modal_if_present()
        # перейти на страницу "Лента заказов"
        page.clic_on_element(TLHP.LOCATOR_BUTTON_ORDER_FEED)
        # проверить, что открылась страница "Лента заказов"
        current_url = driver.current_url
        expected_url = TestUrl.URL_PAGE_ORDER_FEED
        assert current_url == expected_url


    @allure.title('Проверка, что если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_ingredient_details_modal_window(self, driver):
        page = HomePage(driver)
        # закрыть модальное окно
        page.close_modal_if_present()
        # проскролить и кликнуть на "Соус Spicy-X"
        page.scroll_to_element(TLHP.LOCATOR_SAUCE_SPICY_X_BUTTON)
        assert page.is_element_present(TLHP.LOCATOR_CLOSE_SAUCE_SPICY_X_WINDOW)


    @allure.title('Проверка, что всплывающее окно ингредиента закрывается кликом по крестику')
    def test_close_ingredient_modal_window(self, driver):
        page = HomePage(driver)
        # закрыть модальное окно
        page.close_modal_if_present()
        # проскролить и кликнуть на "Соус Spicy-X"
        page.scroll_to_element(TLHP.LOCATOR_SAUCE_SPICY_X_BUTTON)
        # кликнуть на крестик модального окна
        page.clic_on_element(TLHP.LOCATOR_CLOSE_SAUCE_SPICY_X_WINDOW)
        assert  page.is_element_not_visible(TLHP.LOCATOR_SAUCE_SPICY_X_WINDOW)


    @allure.title('Проверка, что при добалении ингредиента в бургер, меняется стоимость бургера')
    def test_put_ingredient_in_order(self, driver):
        page = HomePage(driver)
        # закрыть модальное окно
        page.close_modal_if_present()
        # положить "Краторная булка N-200i" в заказ
        page.drag_and_drop_element(TLHP.LOCATOR_KRATORNAYA_BULKA, TLHP.LOCATOR_OF_SELECTED)
        assert page.get_text_from_element(TLHP.LOCATOR_PRICE) == TD.TEXT_PRICE_KRATORNAYA_BULKA_IN_ORDER



    @allure.title('Проверка, что залогиненный пользователь может оформить заказ')
    def test_place_an_order(self, driver, create_and_delete_user_with_data):
        page = AccountPage(driver)
        # войти в личный кабинет
        page.open_user_page(create_and_delete_user_with_data)
        # перейти в "Конструктор"
        page.clic_on_element(TLHP.LOCATOR_BUTTON_CONSTRUCTOR)
        # нажать на кнопку "Оформить заказ"
        page.clic_on_element(TLHP.LOCATOR_BUTTON_PLACE_AN_ORDER)
        assert page.is_element_present(TLHP.LOCATOR_MODAL_WINDOW_ORDER)