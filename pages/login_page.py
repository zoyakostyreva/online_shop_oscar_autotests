from .base_page import BasePage
from ..constants import TestsUserDataConstants
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login link is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self):
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        input_email.send_keys(TestsUserDataConstants.generate_correct_email())

        input_password1 = self.browser.find_element(*LoginPageLocators.PASSWORD1_FIELD)
        input_password1.send_keys(TestsUserDataConstants.TEST_PASSWORD_CORRECT)
        input_password2 = self.browser.find_element(*LoginPageLocators.PASSWORD2_FIELD)
        input_password2.send_keys(TestsUserDataConstants.TEST_PASSWORD_CORRECT)

        button_submit = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        button_submit.click()

        message = self.browser.find_element(*LoginPageLocators.REGISTRATION_ALERT)
        assert "Thanks for registering!" in message.text, "Should be registration success message"

    def should_be_correct_email(self):
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        input_email.send_keys(TestsUserDataConstants.TEST_EMAIL_INCORRECT)

        input_password1 = self.browser.find_element(*LoginPageLocators.PASSWORD1_FIELD)
        input_password1.send_keys(TestsUserDataConstants.TEST_PASSWORD_CORRECT)
        input_password2 = self.browser.find_element(*LoginPageLocators.PASSWORD2_FIELD)
        input_password2.send_keys(TestsUserDataConstants.TEST_PASSWORD_CORRECT)

        button_submit = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        button_submit.click()

        message = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        assert message.get_attribute(LoginPageLocators.EMAIL_VALIDATION_ATTRIBUTE) is not None, \
            "Проверка на символ @ не была осуществлена"

    def should_be_correct_password_length(self):
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        input_email.send_keys(TestsUserDataConstants.generate_correct_email())

        input_password1 = self.browser.find_element(*LoginPageLocators.PASSWORD1_FIELD)
        input_password1.send_keys(TestsUserDataConstants.TEST_PASSWORD_SHORT)
        input_password2 = self.browser.find_element(*LoginPageLocators.PASSWORD2_FIELD)
        input_password2.send_keys(TestsUserDataConstants.TEST_PASSWORD_SHORT)

        button_submit = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        button_submit.click()

        message = self.browser.find_element(*LoginPageLocators.PASSWORD_ERROR_ALERT)
        assert "short" in message.text, "Should be error that the password is too short"

    def should_be_equal_passwords(self):
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        input_email.send_keys(TestsUserDataConstants.generate_correct_email())

        input_password1 = self.browser.find_element(*LoginPageLocators.PASSWORD1_FIELD)
        input_password1.send_keys(TestsUserDataConstants.TEST_PASSWORD_CORRECT)
        input_password2 = self.browser.find_element(*LoginPageLocators.PASSWORD2_FIELD)
        input_password2.send_keys(TestsUserDataConstants.TEST_PASSWORD_INCORRECT)

        button_submit = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        button_submit.click()

        message = self.browser.find_element(*LoginPageLocators.PASSWORD_ERROR_ALERT)
        assert "didn't match" in message.text, "Should be error that the passwords didn't match"

    def validation_of_earlier_registered_user(self):
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        input_email.send_keys(TestsUserDataConstants.TEST_EXISTED_EMAIL)

        input_password1 = self.browser.find_element(*LoginPageLocators.PASSWORD1_FIELD)
        input_password1.send_keys(TestsUserDataConstants.TEST_PASSWORD_CORRECT)
        input_password2 = self.browser.find_element(*LoginPageLocators.PASSWORD2_FIELD)
        input_password2.send_keys(TestsUserDataConstants.TEST_PASSWORD_CORRECT)

        button_submit = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        button_submit.click()

        message = self.browser.find_element(*LoginPageLocators.EMAIL_ERROR_ALERT)
        assert "already" in message.text, "Should be error that the user already exists"
