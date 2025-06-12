import allure

from pages.order_page import OrderPage


class TestOrderFeed:


    @allure.title('Проверить, что если кликнуть на заказ, откроется всплывающее окно с деталями заказа')
    def test_open_window_with_order_details(self, driver):
        page = OrderPage(driver)
        # открыть "Лента Заказов"
        page.open_order_feed()
        # открыть окно с деталями заказа
        page.open_window_order_details()
        assert page.window_order_details_open()


    @allure.title('Проверить, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_order_present_in_order_feed(self, driver, create_and_delete_user_with_data):
        page = OrderPage(driver)
        # залогиниться, создать заказ, закрыть окно заказа
        page.make_an_order(create_and_delete_user_with_data)
        # перейти в личный кабинет
        page.open_page_login()
        # перейти в "Историю заказов"
        page.open_order_history_page()
        # запомнить номер заказа из "Истории заказов"
        order_number = page.order_number_from_order_history()
        # перейти в "Ленту заказов"
        page.transition_to_order_feed()
        assert page.user_order_is_present(order_number)


    @allure.title('Проверить, что при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_done_order_counter_all_time_increased(self, driver, create_and_delete_user_with_data):
        page = OrderPage(driver)
        # закрыть модельное окно
        page.close_modal_if_present()
        # зайти в "Лента заказов"
        page.transition_to_order_feed()
        # запомнить сколько было заказов за все время
        was_total_orders_all_time = page.total_orders_all_time()
        # залогиниться, сделать новый заказ
        page.make_an_order(create_and_delete_user_with_data)
        # зайти в "Лента заказов"
        page.transition_to_order_feed()
        # запомнить актуальное число заказов за все время
        became_total_orders_all_time = page.total_orders_all_time()
        # проверить, что число заказов за все время увеличилось
        assert was_total_orders_all_time < became_total_orders_all_time


    @allure.title('Проверить, что при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_done_order_counter_for_today_increased(self, driver, create_and_delete_user_with_data):
        page = OrderPage(driver)
        # закрыть модельное окно
        page.close_modal_if_present()
        # зайти в "Лента заказов"
        page.transition_to_order_feed()
        # запомнить сколько было заказов за сегодня
        was_total_orders_today = page.total_orders_today()
        # залогиниться, сделать новый заказ
        page.make_an_order(create_and_delete_user_with_data)
        # зайти в "Лента заказов"
        page.transition_to_order_feed()
        # запомнить актуальное число заказов за сегодня
        became_total_orders_today = page.total_orders_today()
        # проверить, что число заказов за все время увеличилось
        assert was_total_orders_today < became_total_orders_today



    @allure.title('Проверить, что после оформления заказа его номер появляется в разделе "В работе"')
    def test_number_created_order_is_in_progress(self, driver, create_and_delete_user_with_data):
        page = OrderPage(driver)
        # создать новый заказ
        user_order_number = page.make_an_order(create_and_delete_user_with_data)
        # перейти в "Лента заказов"
        page.transition_to_order_feed()
        # ждать появления нашего заказа в списке
        order_number_progress = page.user_order_in_progress()
        assert user_order_number == order_number_progress