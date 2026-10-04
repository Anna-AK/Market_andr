from pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver, locators):
        super().__init__(driver)
        self.locators = locators  # Сюда прилетят либо Android, либо iOS локаторы

    def search_product(self, text):
        # Метод один и тот же для всех, но локатор подставится нужный
        self.enter_text(self.locators.SEARCH_FIELD, text)
        self.click(self.locators.CONFIRM_BUTTON)