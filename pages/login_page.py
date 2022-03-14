from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        print(current_url)
        assert LoginPageLocators.LOGIN_URL in current_url != False, "не правильный url"
        #

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "форма логина не найдена"
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "форма регистрации не найдена"
        assert True

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "password"
        print(email)
        print(password)
        input1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        input1.send_keys(email)
        input2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        input2.send_keys(password)
        input3 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        input3.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()

