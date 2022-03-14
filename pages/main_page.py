from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs): # заглушка так как мы все методы перенесли в base_page
        super(MainPage,self).__init__(*args, **kwargs)

