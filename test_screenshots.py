from .pages.product_page import ProductPage
from .pages.constants import UrlConstants

def test_item_page_has_add_basket_button(browser):
    product_page = ProductPage(browser, UrlConstants.CODERS_AT_WORK_PRODUCT_URL)
    product_page.open()
    product_page.should_be_add_to_basket_button()
