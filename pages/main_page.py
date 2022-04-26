from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        """Open link in browser"""
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        """Login link should be visible"""
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not visible"
