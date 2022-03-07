from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators():
    LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BUCKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ADD_CART_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong" )
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE_BEFORE = (By.CLASS_NAME, "price_color")
    PRODUCT_PRICE_AFTER = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
