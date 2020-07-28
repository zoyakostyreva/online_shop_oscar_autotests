from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "a[href*='basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BOOKS_SUBMENU = (By.CSS_SELECTOR, "#browse [href*='books_2']")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.ID, "id_registration-email")
    PASSWORD1_FIELD = (By.ID, "id_registration-password1")
    PASSWORD2_FIELD = (By.ID, "id_registration-password2")
    SUBMIT_BUTTON = (By.NAME, "registration_submit")
    REGISTRATION_ALERT = (By.CSS_SELECTOR, "#messages div.alertinner")
    EMAIL_VALIDATION_ATTRIBUTE = 'validationMessage'
    PASSWORD_ERROR_ALERT = (By.CSS_SELECTOR, "#id_registration-password2 + span.error-block")
    EMAIL_ERROR_ALERT = (By.CSS_SELECTOR, "#id_registration-email + span.error-block")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERTS_STRONG = (By.CSS_SELECTOR, "#messages .alert .alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner > .product_page .product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner > .product_page .product_main .price_color")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")


class BasketPageLocators():
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")


class BookStorePageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    ALERT_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages .alert .alertinner")
