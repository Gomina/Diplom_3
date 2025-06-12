import allure
import pytest

from locators.account_page_locators import TLAP
from locators.home_page_locators import TLHP
from locators.order_page_locators import TLOP
from pages.order_page import OrderPage


class TestOrderFeed:


    @allure.title('Проверить, что если кликнуть на заказ, откроется всплывающее окно с деталями заказа')
    def test_open_window_with_order_details(self, driver):
        page = OrderPage(driver)
        # открыть "Лента Заказов"
        page.open_order_feed()
        # кликнуть первый заказ в левой колонке
        page.clic_on_element(TLOP.LOCATOR_ORDER_LEFT_COLUMN)
        # дождаться, чтобы окно стало видимым
        page.wait_for_element_visible(TLOP.LOCATOR_MODAL_WINDOW_ORDER)
        assert page.is_element_present(TLOP.LOCATOR_MODAL_WINDOW_ORDER)


    @allure.title('Проверить, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_order_present_in_order_feed(self, driver, create_and_delete_user_with_data):
        page = OrderPage(driver)
        # залогиниться, создать заказ, закрыть окно заказа
        page.make_an_order(create_and_delete_user_with_data)
        # перейти в личный кабинет
        page.clic_on_element(TLHP.LOCATOR_PERSONAL_ACCOUNT)
        # перейти в "Историю заказов"
        page.clic_on_element(TLAP.LOCATOR_HISTORY_ORDER)
        # запомнить номер заказа из "Истории заказов"
        order_number = page.get_text_from_element(TLAP.LOCATOR_ORDER_NUMBER)
        # перейти в "Ленту заказов"
        page.clic_on_element(TLHP.LOCATOR_BUTTON_ORDER_FEED)
        # создать локатор для поиска заказа с номером order_number
        order_feed_locator = (TLOP.LOCATOR_ORDER_LEFT_COLUMN[0], TLOP.LOCATOR_ORDER_LEFT_COLUMN[1].format(order_number))
        # найти заказ с номером order_number
        page.find_element_with_wait(order_feed_locator)
        assert page.is_element_present(order_feed_locator)


    @allure.title('Проверить, что при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_done_order_counter_all_time_increased(self, driver, create_and_delete_user_with_data):
        page = OrderPage(driver)
        # закрыть модельное окно
        page.close_modal_if_present()
        # зайти в "Лента заказов"
        page.clic_on_element(TLHP.LOCATOR_BUTTON_ORDER_FEED)
        # запомнить сколько было заказов за все время
        was_total_orders_all_time = page.get_text_from_element(TLOP.LOCATOR_COMPLETED_FOR_ALL_TIME)
        # залогиниться, сделать новый заказ
        page.make_an_order(create_and_delete_user_with_data)
        # зайти в "Лента заказов"
        page.clic_on_element(TLHP.LOCATOR_BUTTON_ORDER_FEED)
        # запомнить актуальное число заказов за все время
        became_total_orders_all_time = page.get_text_from_element(TLOP.LOCATOR_COMPLETED_FOR_ALL_TIME)
        # проверить, что число заказов за все время увеличилось
        assert was_total_orders_all_time < became_total_orders_all_time


    @allure.title('Проверить, что при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_done_order_counter_for_today_increased(self, driver, create_and_delete_user_with_data):
        page = OrderPage(driver)
        # закрыть модельное окно
        page.close_modal_if_present()
        # зайти в "Лента заказов"
        page.clic_on_element(TLHP.LOCATOR_BUTTON_ORDER_FEED)
        # запомнить сколько было заказов за сегодня
        was_total_orders_today = page.get_text_from_element(TLOP.LOCATOR_COMPLETED_FOR_TODAY)
        # залогиниться, сделать новый заказ
        page.make_an_order(create_and_delete_user_with_data)
        # зайти в "Лента заказов"
        page.clic_on_element(TLHP.LOCATOR_BUTTON_ORDER_FEED)
        # запомнить актуальное число заказов за сегодня
        became_total_orders_today = page.get_text_from_element(TLOP.LOCATOR_COMPLETED_FOR_TODAY)
        # проверить, что число заказов за все время увеличилось
        assert was_total_orders_today < became_total_orders_today



    @allure.title('Проверить, что после оформления заказа его номер появляется в разделе В работе')
    def test_number_created_order_is_in_progress(self, driver, create_and_delete_user_with_data):
        page = OrderPage(driver)
        # создать новый заказ
        user_order_number = page.make_an_order(create_and_delete_user_with_data)
        # перейти в "Лента заказов"
        page.clic_on_element(TLHP.LOCATOR_BUTTON_ORDER_FEED)
        # ждать появления нашего заказа в списке
        order_number_progress = page.wait_for_numeric_text_in_element(TLOP.LOCATOR_ORDER_NUMBER)
        assert user_order_number == order_number_progress