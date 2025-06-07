import allure
import time

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.home_page_locators import TLHP
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
        self.clic_on_element(TLHP.LOCATOR_BUTTON_CONSTRUCTOR)
        # Добавляем ингредиент в заказ
        self.drag_and_drop_element(TLHP.LOCATOR_KRATORNAYA_BULKA, TLHP.LOCATOR_OF_SELECTED)
        # Кликаем на размещение заказа
        self.clic_on_element(TLHP.LOCATOR_BUTTON_PLACE_AN_ORDER)
        # Ждём появления реального номера заказа
        order_number = self.wait_for_updated_order_number()
        # Закрываем окно заказа
        self.clic_on_element(TLHP.LOCATOR_CLOSE_ORDER_WINDOW)
        return f"{int(order_number):07d}"


    @allure.step('Ожидание реального номера заказа в окне заказа')
    def wait_for_updated_order_number(self):
        # найти элемент, который содержит возможный номер заказа
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(TLHP.LOCATOR_GET_ORDER_NUMBER)
        )
        # начать циклический опрос элемента, пока не появится реальный номер
        initial_value = element.text
        start_time = time.time()
        while element.text == initial_value or not element.text.isdigit():
            time.sleep(3)
            if time.time() - start_time > 15:
                raise TimeoutException

        # вернуть номер заказа
        return element.text.strip()