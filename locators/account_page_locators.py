from selenium.webdriver.common.by import By

# тестовые локаторы страницы личного кабинета и входа в него
class TLAP:

    # локатор "Восстановить пароль" страница "Вход"
    LOCATOR_RECOVER_PASSWORD = By.XPATH, "//a[contains(text(), 'Восстановить пароль')]"

    # локатор поля "Email". Страница "Восстановление пароля"
    LOCATOR_FIELD_EMAIL = By.XPATH, "//input[@type='text' and @name='name']"

    # локатор кнопки "Восстановить". Страница "Восстановление пароля"
    LOCATOR_BUTTON_RECOVER = By.XPATH, "//button[text()='Восстановить']"

    # локатор поля "Введите код из письма". Страница "Восстановление пароля"
    LOCATOR_FIELD_CODE_FROM_LETTER = By.XPATH, "//label[text()='Введите код из письма']"

    # локатор "глаза" показать/скрыть пароль. Страница "Восстановление пароля"
    LOCATOR_SHOW_HIDE_PASSWORD = By.CSS_SELECTOR, ".input__icon.input__icon-action"

    # локатор синей рамки поля "Пароль". Страница "Восстановление пароля"
    LOCATOR_INPUT_FIELD_BORDER = By.XPATH, "//div[contains(@class, 'input_type_text') and contains(@class, 'input_size_default')]"

    # локатор "История заказов".  Страница "Профиль"
    LOCATOR_HISTORY_ORDER =  By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive' and text()='История заказов']"

    # локатор кнопки "Выход".  Страница "Профиль"
    LOCATOR_BUTTON_LOGOUT = (By.XPATH, "//button[contains(@class, 'Account_button__14Yp3') and text()='Выход']")

    # локатор поля "Email". Страница "Вход"
    LOCATOR_FIELD_EMAIL_LOGIN = By.XPATH, "//input[@type='text']"

    # локатор поля "Пароль". Страница "Вход"
    LOCATOR_FIELD_PASSWORD_LOGIN = By.XPATH, "//input[@type='password']"

    # локатор кнопки "Войти". Страница "Вход"
    LOCATOR_BUTTON_LOGIN = By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Войти']"

    #локатор номера заказа. Страница "История заказов"
    LOCATOR_ORDER_NUMBER = By.XPATH, '//div[@class="OrderHistory_textBox__3lgbs mb-6"]/p[contains(@class, "text_type_digits-default") and starts-with(text(), "#")]'