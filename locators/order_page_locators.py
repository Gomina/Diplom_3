from selenium.webdriver.common.by import By

# локаторы для страницы "Лента Заказов"
class TLOP:

    # локатор 1 заказа в левой части окна
    LOCATOR_ORDER_LEFT_COLUMN = By.XPATH, '//li[contains(@class, "OrderHistory_listItem__2x95r")][1]'

    # локатор окна с деталями заказа
    LOCATOR_MODAL_WINDOW_ORDER = By.XPATH, '//div[contains(@class, "Modal_orderBox__1xWdi") and contains(@class, "Modal_modal__contentBox__sCy8X")]'

    # локатор для поиска заказа из "Истории заказов"
    LOCATOR_ORDER_USER = By.XPATH, '//p[contains(@class, "text_type_digits-default") and contains(text(), "{}")]'

    # локатор количество заказов "Выполнено за все время". Страница "Лента Заказов"
    LOCATOR_COMPLETED_FOR_ALL_TIME = By.XPATH, "//p[contains(@class, 'OrderFeed_number__2MbrQ')]"

    # локатор количество заказов "Выполнено за сегодня". Страница "Лента Заказов"
    LOCATOR_COMPLETED_FOR_TODAY = By.XPATH, "//p[contains(@class, 'OrderFeed_number__2MbrQ')]"

    # локатор заказов в работе. Страница "Лента Заказов"
    LOCATOR_ORDER_IN_PROGRESS = By.CSS_SELECTOR, ".text.text_type_digits-default.mb-2"

    # локатор заказа в работе. Страница "Лента Заказов"
    LOCATOR_ORDER_NUMBER = (By.XPATH, "//li[contains(@class, 'text_type_digits-default')]")