import math
from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """Class contains methods for pages with items"""
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should disappear"

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON).click()

    def check_item_name(self):
        # имя товара до и после добавления в корзину должны быть одинаковы
        name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        name_in_basket = self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_BASKET).text
        assert name == name_in_basket, "Names of item not equal"

    def check_item_cost(self):
        cost = self.browser.find_element(*ProductPageLocators.ITEM_COST).text
        cost_in_basket = self.browser.find_element(*ProductPageLocators.ITEM_COST_IN_BASKET).text
        assert cost == cost_in_basket, "Costs of item not equal"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
