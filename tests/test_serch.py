from pages.main_page import MainPage


def test_product_search(app_context):
    driver = app_context["driver"]
    locators = app_context["locators"]

    # Создаем страницу, передавая в нее динамический контекст
    main_page = MainPage(driver, locators)

    # Шаг теста
    main_page.search_product("Смартфон Android")

    # Дальше проверка (Assert)...