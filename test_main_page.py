import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.skip(reason="no need in this test right now")
def test_guest_can_go_to_login_page(browser):
    """Testing that user can open login page"""
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)     # инициализируем PageObject
    main_page.open()
    main_page.go_to_login_page()    # переходим на страницу регистрации
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.skip(reason="no need in this test right now")
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_basket_page()
    basket_page = BasketPage(browser, link)
    basket_page.basket_is_empty()
    basket_page.basket_is_empty_message_presented()
