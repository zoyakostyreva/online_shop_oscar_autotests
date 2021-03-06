from .constants import UrlConstants
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import time
import pytest


@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, UrlConstants.LOGIN_URL)
        login_page.open()
        login_page.should_be_login_page()
        login_page.register_new_user()
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, UrlConstants.CODERS_AT_WORK_PRODUCT_URL)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, UrlConstants.CODERS_AT_WORK_PRODUCT_URL)
        page.open()
        page.click_add_to_basket_button()
        page.product_is_present_in_basket()
        page.alert_price_is_equal_to_product_price()


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"{link}"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    time.sleep(2)
    page.product_is_present_in_basket()
    page.alert_price_is_equal_to_product_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, UrlConstants.CODERS_AT_WORK_PRODUCT_URL)
    page.open()
    page.click_add_to_basket_button()
    page.should_not_be_success_message_after_adding_to_basket()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, UrlConstants.CODERS_AT_WORK_PRODUCT_URL)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, UrlConstants.CODERS_AT_WORK_PRODUCT_URL)
    page.open()
    page.click_add_to_basket_button()
    page.success_message_is_disappeared_after_adding_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, UrlConstants.CODERS_AT_WORK_PRODUCT_URL)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, UrlConstants.CITY_AND_STARTS_PRODUCT_URL)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, UrlConstants.CITY_AND_STARTS_PRODUCT_URL)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_is_empty_message()
    basket_page.no_items_in_basket()

