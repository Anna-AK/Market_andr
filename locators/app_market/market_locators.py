from appium.webdriver.common.appiumby import AppiumBy


class MarketMainLocators:
    # Кнопка/поле поиска на главном экране (обычно имеет id или доступный текст)
    SEARCH_INPUT_FIELD = (AppiumBy.ID, "ru.yandex.market:id/search_text_input")

    # Кнопка подтверждения поиска на клавиатуре или лупа в приложении
    SEARCH_BUTTON = (AppiumBy.ID, "ru.yandex.market:id/search_button")

    # Заголовок на экране результатов поиска, чтобы проверить, что мы перешли куда надо
    SEARCH_RESULT_TITLE = (AppiumBy.ID, "ru.yandex.market:id/result_title")
