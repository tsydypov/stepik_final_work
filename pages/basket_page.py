from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    """Class contains methods for basket page"""
    def basket_is_empty(self):
        # проверка, что в корзине нет товаров
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), \
            "Basket contains items but should be empty"

    def basket_is_empty_message_presented(self):
        # есть текст о пустой корзине, сравнивать текст не нужно, важно само наличие
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Message about empty basket is not found"
