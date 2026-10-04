from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # Установим дефолтное время ожидания элементов в 10 секунд
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator):
        """Безопасный поиск элемента с явным ожиданием его появления на экране"""
        # Преобразуем наш кортеж локатора (например, ("id", "element_id")) для Appium
        by_type, value = locator
        return self.wait.until(EC.presence_of_element_by_locator((by_type, value)))

    def click(self, locator):
        """Дожидается элемента и кликает по нему"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text):
        """Дожидается текстового поля, очищает его и вводит текст"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator):
        """Возвращает текст элемента (например, для проверок assert в тестах)"""
        return self.find_element(locator).text