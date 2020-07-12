from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    # def should_be_add_to_basket_button(self):
    #     assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"

    def click_add_to_basket_button(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def product_is_present_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        alert_product_in_basket = self.find_element(*ProductPageLocators.ALERT_PRODUCT_IN_BASKET)
        assert product_name.text in alert_product_in_basket.text, "Product isn't in the basket"

    def alert_price_is_equal_to_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        alert_price_in_basket = self.find_element(*ProductPageLocators.ALERT_PRICE_IN_BASKET)
        assert product_price.text in alert_price_in_basket.text, f"Price in basket {alert_price_in_basket.text} " \
                                                                 f"isn't equal to product price {product_price.text}"


