from .base_page import BasePage
from .locators import BasePageLocators


class MainPage(BasePage):
    def go_to_book_store_page(self):
        book_submenu = self.browser.find_element(*BasePageLocators.BOOKS_SUBMENU)
        book_submenu.click()

