from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "a[href*='basket']")

# class MainPageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner strong")
    ALERT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) .alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner > .product_page .product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner > .product_page .product_main .price_color")

class BasketPageLocators():
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")

