from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):  # метод добавления в корзину
        bucket_buttom = self.browser.find_element(*ProductPageLocators.ADD_TO_BUCKET_BUTTON)
        bucket_buttom.click()

    def product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name

    def product_price(self):
        product_price_before = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_BEFORE)
        return product_price_before

    def checking_add_to_cart_message(self, product_name):  # Содежит ли сообщение название добаленного в карзину товара
        message_text_after_add_to_bucket = self.browser.find_element(*ProductPageLocators.ADD_CART_MESSAGE)
        assert product_name.text == message_text_after_add_to_bucket.text, f"Название добавленного товара {product_name.text}, но в сообщении указано название {message_text_after_add_to_bucket.text}"

    def price_check_after_adding_to_kart(self, product_price_before): # Проверка корректности отображения общей цены после добавления товара
        product_price_after = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_AFTER)
        assert product_price_before.text in product_price_after.text, "Не совпадают"
        print(f"Цена товара на странице: {product_price_before.text}, Общая цена корзины: {product_price_after.text}")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_CART_MESSAGE), \
            "Success message is presented, but should not be"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_CART_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_CART_MESSAGE), \
            "The message did not disappear"