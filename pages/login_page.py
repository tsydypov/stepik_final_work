import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert 'login' in current_url, "Current URL doesn't contain 'login'"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login form not found"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REG_FORM), "Register form not found"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "password"
        email_form = self.browser.find_element(*LoginPageLocators.EMAIL_FORM)
        email_form.send_keys(email)
        password_form = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM)
        password_form.send_keys(password)
        password_confirm_form = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM_FORM)
        password_confirm_form.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()
