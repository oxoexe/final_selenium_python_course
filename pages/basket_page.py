from .base_page import BasePage
from .locators import BasketPageLocators

class BasePage(BasePage):
    def shold_be_empty_basket_text(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT) != False, "No text that the basket is empty "

    def should_be_emty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PROD_IN_BASKET_TEXT), "Basket is not empty"