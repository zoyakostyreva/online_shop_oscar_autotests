import time
from os import getenv


class UrlConstants():
    BASE_URL = getenv('BASE_URL', 'http://selenium1py.pythonanywhere.com')
    LOGIN_URL = f"{BASE_URL}/accounts/login/"
    CODERS_AT_WORK_PRODUCT_URL = f"{BASE_URL}/catalogue/coders-at-work_207"
    CITY_AND_STARTS_PRODUCT_URL = f"{BASE_URL}/catalogue/the-city-and-the-stars_95/"


class TestsConstants():
    WINDOW_SIZE = ('1280', '720')


class TestsUserDataConstants():
    TEST_EMAIL_INCORRECT = 'kostyreva'
    TEST_EXISTED_EMAIL = 'user2@gmail.com'
    TEST_PASSWORD_CORRECT = '12Password!'
    TEST_PASSWORD_SHORT = '12'
    TEST_PASSWORD_INCORRECT = '12Password'

    @classmethod
    def generate_correct_email(cls):
        generated_email = str(time.time()) + "@fakemail.org"
        print(generated_email)
        return generated_email
