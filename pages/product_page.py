from telnetlib import EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
                                                 "Add to basket button is not presented"

    def click_add_to_basket_button(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def product_is_present_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        alerts_product_in_basket = self.browser.find_elements(*ProductPageLocators.ALERTS_STRONG)
        assert any(product_name.text == element.text for element in alerts_product_in_basket), \
            "Product isn't in the basket"

    def alert_price_is_equal_to_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        alerts_price_in_basket = self.browser.find_elements(*ProductPageLocators.ALERTS_STRONG)
        assert any(product_price.text == element.text for element in alerts_price_in_basket), \
            f"Price in basket isn't equal to product price {product_price.text}"

    def should_not_be_success_message_after_adding_to_basket(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"

    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared_after_adding_to_basket(self, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located(*ProductPageLocators.SUCCESS_MESSAGE))
        except TimeoutException:
            return False

        return True

