from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    """Testing that user can open login page"""
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)     # инициализируем PageObject
    main_page.open()    # открываем главную страницу, функция наследована от класса MainPage
    main_page.go_to_login_page()    # переходим на страницу регистрации


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_login_link()
