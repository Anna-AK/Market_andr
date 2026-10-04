import pytest
from drivers.driver_factory import DriverFactory
from locators.app_market import market_locators #, ios_locators


def pytest_addoption(parser):
    # Добавляем аргументы в консоль: --platform и --app
    parser.addoption("--platform", action="store", default="android", help="android or ios")
    parser.addoption("--app", action="store", default="market", help="market or delivery")


@pytest.fixture(scope="function")
def app_context(request):
    platform = request.config.getoption("--platform").lower()
    app_name = request.config.getoption("--app").lower()

    # 1. Инициализируем нужный драйвер через фабрику
    driver = DriverFactory.get_driver(platform, app_name)

    # 2. Выбираем нужный набор локаторов динамически
    if app_name == "market":
        locators = android_locators.MarketMainLocators if platform == "android" else ios_locators.MarketMainLocators
    else:
        # Тут будет логика для второго приложения
        pass

    yield {"driver": driver, "locators": locators}

    driver.quit()