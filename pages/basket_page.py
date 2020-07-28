from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_is_empty_message(self):
        message = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE)
        assert "is empty" in message.text, "Basket is not empty"

    def no_items_in_basket(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_ITEM), \
            "There are some items in the basket, but should not be"
