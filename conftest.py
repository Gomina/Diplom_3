import pytest
import allure

from selenium import webdriver

from data import TU
from helper import UserMethods


@allure.step('метод для запуска драйвера Firefox и открытие сайта на главной странице')
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
	main_site = 'https://stellarburgers.nomoreparties.site'

	if request.param == "chrome":
		from selenium.webdriver.chrome.options import Options
		chrome_options = Options()
		# критически важные настройки для отключения уведомлений - отключить проверку утечек паролей
		chrome_options.add_experimental_option("prefs", {
			"profile.password_manager_leak_detection": False
		})
		driver = webdriver.Chrome(options=chrome_options)
		driver.set_window_size(1920, 1080)

	elif request.param == "firefox":
		driver = webdriver.Firefox()
		driver.set_window_size(1280, 720)

	driver.get(main_site)
	yield driver
	driver.quit()


@allure.step('метод создает пользователя c заданными данными и удаляет его после теста')
@pytest.fixture
def create_and_delete_user_with_data():
	user_data = TU.User_1
	usermethods = UserMethods()
	# создание пользователя
	created_data = usermethods.create_user(
        email=user_data["email"],
        password=user_data["password"],
        name=user_data["name"]
    )
	yield created_data
	# удаление пользователя после завершения теста
	token = created_data["response"].json().get("accessToken")
	usermethods.delete_user(token)

