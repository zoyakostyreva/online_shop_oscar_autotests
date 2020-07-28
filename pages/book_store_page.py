from .base_page import BasePage
from .locators import BookStorePageLocators


class BookStorePage(BasePage):
    def click_add_to_basket_button(self):
        basket_button = self.browser.find_element(*BookStorePageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def product_is_present_in_basket(self):
        alerts_product_in_basket = self.browser.find_elements(*BookStorePageLocators.ALERT_PRODUCT_IN_BASKET)
        assert any("added to your basket" in element.text for element in alerts_product_in_basket), \
            "Alert product is added to basket is not correct"
