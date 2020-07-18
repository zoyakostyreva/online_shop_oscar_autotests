import pytest
from .pages.constants import UrlConstants
from .pages.login_page import LoginPage

def test_guest_should_be_on_login_page(browser):
    login_page = LoginPage(browser, UrlConstants.LOGIN_URL)
    login_page.open()
    login_page.should_be_login_url()

def test_guest_should_see_login_form(browser):
    login_page = LoginPage(browser, UrlConstants.LOGIN_URL)
    login_page.open()
    login_page.should_be_login_form()

def test_guest_should_see_register_form(browser):
    login_page = LoginPage(browser, UrlConstants.LOGIN_URL)
    login_page.open()
    login_page.should_be_register_form()

@pytest.mark.need_review_custom_scenarios
def test_email_should_be_correct(browser):
    login_page = LoginPage(browser, UrlConstants.LOGIN_URL)
    login_page.open()
    login_page.should_be_correct_email()

@pytest.mark.need_review_custom_scenarios
def test_password_should_be_correct_length(browser):
    login_page = LoginPage(browser, UrlConstants.LOGIN_URL)
    login_page.open()
    login_page.should_be_correct_password_length()

@pytest.mark.need_review_custom_scenarios
def test_passwords_should_be_equal(browser):
     login_page = LoginPage(browser, UrlConstants.LOGIN_URL)
     login_page.open()
     login_page.should_be_equal_passwords()

@pytest.mark.need_review_custom_scenarios
def test_user_should_be_registered(browser):
    login_page = LoginPage(browser, UrlConstants.LOGIN_URL)
    login_page.open()
    login_page.should_be_login_page()
    login_page.register_new_user()
    login_page.should_be_authorized_user()

@pytest.mark.need_review_custom_scenarios
def test_user_already_registered(browser):
    login_page = LoginPage(browser, UrlConstants.LOGIN_URL)
    login_page.open()
    login_page.should_be_login_page()
    login_page.validation_of_earlier_registered_user()

