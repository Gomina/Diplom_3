import allure

from selenium.webdriver.support.wait import WebDriverWait

from locators.account_page_locators import TLAP
from locators.home_page_locators import TLHP
from locators.order_page_locators import TLOP
from pages.account_page import AccountPage


class OrderPage (AccountPage):

    @allure.step('Перейти на страницу "Лента Заказов"')
    def open_order_feed(self):
        # дождаться закрытия модального окна
        self.close_modal_if_present()
        # кликнуть "Лента Заказов"
        self.clic_on_element(TLHP.LOCATOR_BUTTON_ORDER_FEED)


    @allure.step('Оформить заказ')
    def make_an_order(self, create_and_delete_user_with_data):
        # Закрываем модальные окна
        self.close_modal_if_present()
        # Открываем страницу пользователя
        self.open_user_page(create_and_delete_user_with_data)
        # Переходим в Конструктор
        self.close_modal_if_present()
        self.clic_on_element(TLHP.LOCATOR_BUTTON_CONSTRUCTOR)
        # Добавляем ингредиент в заказ
        self.drag_and_drop_element(TLHP.LOCATOR_KRATORNAYA_BULKA, TLHP.LOCATOR_OF_SELECTED)
        # Кликаем на размещение заказа
        self.clic_on_element(TLHP.LOCATOR_BUTTON_PLACE_AN_ORDER)
        # Ждём появления реального номера заказа
        order_number = self.wait_for_updated_order_number()
        # Закрываем окно заказа
        self.clic_on_element(TLHP.LOCATOR_CLOSE_ORDER_WINDOW)
        self.close_modal_if_present()
        return f"{int(order_number):07d}"


    @allure.step('Открыть окно детали заказа в "Ленте заказа"')
    def open_window_order_details(self):
        # кликнуть первый заказ в левой колонке
        self.clic_on_element(TLOP.LOCATOR_ORDER_LEFT_COLUMN)
        # дождаться, чтобы окно стало видимым
        self.wait_for_element_visible(TLOP.LOCATOR_MODAL_WINDOW_ORDER)


    @allure.step('Окно детали заказа в "Ленте заказа" открыто')
    def window_order_details_open(self):
        return self.is_element_present(TLOP.LOCATOR_MODAL_WINDOW_ORDER)


    @allure.step('Запомнить номер заказа из "Истории заказов"')
    def order_number_from_order_history(self):
        return self.get_text_from_element(TLAP.LOCATOR_ORDER_NUMBER)


    @allure.step('Найти номер заказа клиента из "Истории заказов" в "Ленте заказов"')
    def user_order_is_present(self,order_number):
        # создать локатор для поиска заказа с номером order_number
        order_feed_locator = (TLOP.LOCATOR_ORDER_LEFT_COLUMN[0], TLOP.LOCATOR_ORDER_LEFT_COLUMN[1].format(order_number))
        # найти заказ с номером order_number
        self.find_element_with_wait(order_feed_locator)
        return self.is_element_present(order_feed_locator)

    @allure.step('Метод возвращает число заказов из графы "Выполнено за все время". Страница "Лента заказов"')
    def total_orders_all_time(self):
        return self.get_text_from_element(TLOP.LOCATOR_COMPLETED_FOR_ALL_TIME)

    @allure.step('Метод возвращает число заказов из графы "Выполнено за сегодня". Страница "Лента заказов"')
    def total_orders_today(self):
        return self.get_text_from_element(TLOP.LOCATOR_COMPLETED_FOR_TODAY)

    @allure.step('Найти номер заказа клиента в "В работе" в "Ленте заказов"')
    def user_order_in_progress(self):
        return self.wait_for_numeric_text_in_element(TLOP.LOCATOR_ORDER_NUMBER)