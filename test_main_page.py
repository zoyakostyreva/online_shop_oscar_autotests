import pytest
from .constants import UrlConstants
from .pages.book_store_page import BookStorePage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = BasePage(browser, UrlConstants.BASE_URL)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = BasePage(browser, UrlConstants.BASE_URL)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasePage(browser, UrlConstants.BASE_URL)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_is_empty_message()
    basket_page.no_items_in_basket()


@pytest.mark.need_review_custom_scenarios
def test_guest_can_add_product_to_basket_from_main_page(browser):
    main_page = MainPage(browser, UrlConstants.BASE_URL)
    main_page.open()
    main_page.go_to_book_store_page()
    book_store_page = BookStorePage(browser, browser.current_url)
    book_store_page.click_add_to_basket_button()
    book_store_page.product_is_present_in_basket()
