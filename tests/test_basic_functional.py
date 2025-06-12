import allure

from pages.account_page import AccountPage
from pages.home_page import HomePage


class TestBasicFunctions:


    @allure.title('Проверка перехода по клику на «Конструктор»')
    def test_transition_to_constructor(self, driver):
        page = HomePage(driver)
        # закрыть модальное окно
        page.close_modal_if_present()
        # открыть страницу "Конструктор" и запомнить её URL
        current_url = page.transition_to_constructor()
        # URL, который должен быть у страницы "Конструктор"
        expected_url = page.expected_url_constructor()
        assert current_url == expected_url


    @allure.title('Проверка перехода по клику на  «Лента заказов»')
    def test_transition_to_order_feed(self, driver):
        page = HomePage(driver)
        # закрыть модальное окно
        page.close_modal_if_present()
        # открыть страницу "Лента заказов" и запомнить её URL
        current_url = page.transition_to_order_feed()
        # URL, который должен быть у страницы "Лента заказов"
        expected_url = page.expected_url_order_feed()
        assert current_url == expected_url


    @allure.title('Проверка, что если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_ingredient_details_modal_window(self, driver):
        page = HomePage(driver)
        # закрыть модальное окно
        page.close_modal_if_present()
        # открыть окно с деталями ингредиента "Соус Spicy-X"
        page.open_window_ingredient_detail_SPICY_X()
        assert page.window_ingredient_detail_SPICY_X_present()


    @allure.title('Проверка, что всплывающее окно ингредиента закрывается кликом по крестику')
    def test_close_ingredient_modal_window(self, driver):
        page = HomePage(driver)
        # закрыть модальное окно
        page.close_modal_if_present()
        # открыть окно с деталями ингредиента "Соус Spicy-X"
        page.open_window_ingredient_detail_SPICY_X()
        # закрыть модальное окно
        page.close_window_ingredient_detail_SPICY_X()
        assert  page.window_ingredient_detail_SPICY_X_not_visible()


    @allure.title('Проверка, что при добалении ингредиента в бургер, меняется стоимость бургера')
    def test_put_ingredient_in_order(self, driver):
        page = HomePage(driver)
        # закрыть модальное окно
        page.close_modal_if_present()
        # положить "Краторная булка N-200i" в заказ и оценить стоимость
        real_value = page.throw_bun_in_order_price()
        assert real_value == page.cost_two_Kratornaya_bun_N_200i()


    @allure.title('Проверка, что залогиненный пользователь может оформить заказ')
    def test_place_an_order(self, driver, create_and_delete_user_with_data):
        page = AccountPage(driver)
        # войти в личный кабинет
        page.open_user_page(create_and_delete_user_with_data)
        # перейти в "Конструктор"
        page.transition_to_constructor()
        # нажать на кнопку "Оформить заказ"
        page.open_order_window()
        assert page.order_window_open()