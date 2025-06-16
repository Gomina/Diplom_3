from selenium.webdriver.common.by import By

# тестовые локаторы домашней страницы
class TLHP:

    # локатор кнопки "Личный кабинет" в шапке сайта
    LOCATOR_PERSONAL_ACCOUNT = By.XPATH, '//a[.//p[text()="Личный Кабинет"]]'

    # локатор модального окна на домашней странице
    LOCATOR_MODAL_WINDOW = By.CSS_SELECTOR, "div[class*='modal_overlay']"

    # локатор кнопки закрытия модального окна на домашней странице
    LOCATOR_BUTTON_MODAL_WINDOW = By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr button"

    # локатор кнопки "Конструктор" в шапке сайта
    LOCATOR_BUTTON_CONSTRUCTOR = By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2"][contains(text(), "Конструктор")]'

    # локатор кнопки "Лента Заказов" в шапке сайта
    LOCATOR_BUTTON_ORDER_FEED = By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2"][contains(text(), "Лента Заказов")]'

    # локатор "Соус Spicy-X"
    LOCATOR_SAUCE_SPICY_X_BUTTON = By.XPATH, '//a[img[@alt="Соус Spicy-X"]]'

    # локатор всплывающего окна "Соус Spicy-X"
    LOCATOR_SAUCE_SPICY_X_WINDOW = By.XPATH, '//h2[contains(text(), "Детали ингредиента")]'

    # локатор "крестика" всплывающего окна "Соус Spicy-X"
    LOCATOR_CLOSE_SAUCE_SPICY_X_WINDOW = By.XPATH, '//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]'

    # локатор "Краторная булка"
    LOCATOR_KRATORNAYA_BULKA = By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]'

    # локатор "Перетяните булку сюда"
    LOCATOR_OF_SELECTED = By.CSS_SELECTOR, '.BurgerConstructor_basket__29Cd7'

    # локатор стоимости собранного бургера
    LOCATOR_PRICE = By.XPATH, '//p[@class="text text_type_digits-medium mr-3"]'

    # локатор кнопки "Оформить заказ"
    LOCATOR_BUTTON_PLACE_AN_ORDER = By.XPATH, '//button[contains(@class, "button_button__33qZ0") and contains(text(), "Оформить заказ")]'

    # локатор окна заказа
    LOCATOR_MODAL_WINDOW_ORDER = By.XPATH, '//div[contains(@class, "Modal_modal__contentBox__sCy8X") and .//p[contains(text(), "идентификатор заказа")]]'

    # локатор окна заказа, для получения номера заказа
    LOCATOR_GET_ORDER_NUMBER = By.CSS_SELECTOR, '.Modal_modal__title_shadow__3ikwq'

    # локатор закрытия окна заказа на странице "Конструктор"
    LOCATOR_CLOSE_ORDER_WINDOW = By.XPATH, "//button[contains(@class, 'Modal_modal__close')]"


    # локатор оверлея окна заказа на странице "Конструктор"
    LOCATOR_OVERLAY_WINDOW_ORDER = By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"