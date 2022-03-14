from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasePage
import pytest

@pytest.mark.login_quest
class TestLoginFromMainPage():
    # незабываем передать первым аргументом self
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        # page.should_be_login_link()      # проверяем наличие ссылки
        page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)  # инициализируем LoginPage
        login_page.should_be_login_page()  # запуск метода LoginPage для проверки url, login формы и register формы

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket()
        basket_page = BasePage(browser, browser.current_url)
        basket_page.shold_be_empty_basket_text()
        basket_page.should_be_emty_basket()