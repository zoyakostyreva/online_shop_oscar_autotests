from .base_page import BasePage
from .locators import BookStorePageLocators

class BookStorePage(BasePage):
    def click_add_to_basket_button(self):
        basket_button = self.browser.find_element(*BookStorePageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def product_is_present_in_basket(self):
        alert_product_in_basket = self.browser.find_element(*BookStorePageLocators.ALERT_PRODUCT_IN_BASKET)
        assert "added to your basket" in alert_product_in_basket.text, \
                              "Alert product is added to basket is not correct"