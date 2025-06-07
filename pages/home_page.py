import allure

from selenium.common import TimeoutException, NoSuchElementException
from seletools.actions import drag_and_drop
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.home_page_locators import TLHP


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        # создать экземпляр WebDriverWait с таймаутом 10 секунд
        self.wait = WebDriverWait(self.driver, 10)


    @allure.step('метод находить нужный элемент')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located(locator)
        )
        return self.driver.find_element(*locator)


    @allure.step('метод кликает по нужному элементы')
    def clic_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()


    @allure.step('метод скроллит до нужного элемента и кликает его')
    def scroll_to_element(self, locator):
        # дождаться появления элемента на странице
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(locator)
        )
        # прокрутить до элемента
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # кликнуть по элементу через JavaScript
        self.driver.execute_script("arguments[0].click();", element)
        # возврат найденного элемента
        return element


    @allure.step('метод возвращает текст элементы')
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text


    @allure.step('метод вставляет текст в элемент')
    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    @allure.step('метод ожидает загрузку элемента с числовым текстом')
    def wait_for_numeric_text_in_element(self, locator):
        element = WebDriverWait(self.driver, 20).until(
            lambda driver: driver.find_element(*locator)
        )
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*locator).text.strip().isdigit()
        )
        return element.text


    @allure.step('метод ожидает загрузку конкретного url')
    def loading_page_with_url(self, url):
        WebDriverWait(self.driver, 10).until(
            EC.url_contains(url)
        )


    @allure.step('метод переносит ингредиент в корзину')
    def drag_and_drop_element(self, source, target):
        source_element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(source)
        )
        target_element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(target)
        )
        drag_and_drop(self.driver, source_element, target_element)



    @allure.step('метод закрывает модальное окно, если оно есть')
    def close_modal_if_present(self):
        try:
            # дождаться появления модального окна
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(TLHP.LOCATOR_MODAL_WINDOW)
            )
            # найти кнопку закрытия внутри окна и кликнуть её
            WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable(TLHP.LOCATOR_BUTTON_MODAL_WINDOW)
            ).click()
            # дождаться исчезновения окна
            WebDriverWait(self.driver, 2).until(
                EC.invisibility_of_element_located(TLHP.LOCATOR_MODAL_WINDOW)
            )
        except TimeoutException:
            # если окно не появилось за 2 секунды - продолжить
            pass


    @allure.step('метод ожидает видимость элемента')
    def wait_for_element_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )


    @allure.step('метод проверяет, что элемент отсутствует (не виден) на странице')
    def is_element_not_visible(self, locator):
        try:
            WebDriverWait(self.driver, 1).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False


    @allure.step('метод проверяет, что элемент присутствует')
    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False