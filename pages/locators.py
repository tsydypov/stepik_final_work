from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REG_FORM = (By.CSS_SELECTOR, ".register_form")


class ProductPageLocators:
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    ITEM_NAME_IN_BASKET = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    ITEM_COST = (By.CSS_SELECTOR, ".product_main > .price_color")
    ITEM_COST_IN_BASKET = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
