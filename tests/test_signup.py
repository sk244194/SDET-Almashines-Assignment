import time
from pages.signup import SignupPage
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.signup import SignupPage


def test_existing_user(driver):

    signup = SignupPage(driver)

    signup.enter_email("shubkr244@gmail.com")

    result = signup.click_continue()

    assert result == "existing_user"


import time
from pages.signup import SignupPage

# For Signup
def test_new_user(driver):

    signup = SignupPage(driver)

    # OTP Checking
    # email = "focop80711@ezimb.com"
    email = f"test{int(time.time())}@gmail.com"

    signup.enter_email(email)

    result = signup.click_continue()

    assert result == "new_user"

    signup.enter_first_name("Shubham")
    signup.enter_last_name("Kumar")
    signup.enter_password("Password@123")
    signup.enter_confirm_password("Password@123")

    signup.click_signup()

    # Not sure how to fetch OTP through API
    otp = input("Enter OTP: ")

    signup.enter_otp(otp)

    signup.click_verify()

    signup.select_role()

    signup.select_joining_year(2021)

    signup.select_graduation_year(2025)

    signup.accept_terms()

    signup.accept_privacy()

    signup.click_join()


def test_invalid_email(driver):

    signup = SignupPage(driver)

    signup.enter_email("abc")

    signup.click_continue()

    assert signup.get_email_error() == "Please enter a valid E-mail Address"