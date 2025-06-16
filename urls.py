from selenium.webdriver.common.by import By

class TestUrl:

    # URL главной (домашней) страницы "Stellar Burgers"
    URL_HOME_PAGE_STELLAR_BURGERS = 'https://stellarburgers.nomoreparties.site'

    # URL страницы "Восстановление пароля"
    URL_PAGE_RECOVER_PASSWORD = 'https://stellarburgers.nomoreparties.site/forgot-password'

    # URL страницы "Вход"
    URL_PAGE_LOGIN = 'https://stellarburgers.nomoreparties.site/login'

    # URL создание пользователя для API
    CREATE_USER = 'https://stellarburgers.nomoreparties.site/api/auth/register'

    # URL удаления пользователя для API
    DELETE_USER = 'https://stellarburgers.nomoreparties.site/api/auth/user'

    # URL страницы "История заказов"
    URL_HISTORY_ORDER = 'https://stellarburgers.nomoreparties.site/account/order-history'

    # URL страницы "Конструктор"
    URL_PAGE_CONSTRUCTOR = 'https://stellarburgers.nomoreparties.site/'

    # URL страницы "Лента Заказов"
    URL_PAGE_ORDER_FEED = 'https://stellarburgers.nomoreparties.site/feed'