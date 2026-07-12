from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class SignupPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    email_input = (By.ID, "email")
    continue_btn = (By.ID, "emailBtn")

    first_name = (By.ID, "fname")
    last_name = (By.ID, "lname")
    password = (By.ID, "password")
    confirm_password = (By.ID, "re-password")

    existing_user_msg = (By.ID, "passwordLogin")

    email_error = (By.CSS_SELECTOR, "span.mdl-textfield__error")

    def enter_email(self, email):
        self.wait.until(
            EC.visibility_of_element_located(self.email_input)
        ).send_keys(email)

    def click_continue(self):
        self.wait.until(
        EC.element_to_be_clickable(self.continue_btn)).click()
        
        self.wait.until(
            lambda driver:
                (
                    driver.find_elements(*self.first_name)
                    and driver.find_elements(*self.first_name)[0].is_displayed()
                )
                or
                (
                    driver.find_elements(*self.existing_user_msg)
                    and driver.find_elements(*self.existing_user_msg)[0].is_displayed()
                )
                or
                (
                    driver.find_elements(*self.email_error)
                    and driver.find_elements(*self.email_error)[0].is_displayed()
                )
        )

        if len(self.driver.find_elements(*self.existing_user_msg)) > 0:
            return "existing_user"

        if len(self.driver.find_elements(*self.first_name)) > 0:
            return "new_user"

        return "validation_error"

    def enter_first_name(self, name):
        self.driver.find_element(*self.first_name).send_keys(name)

    def enter_last_name(self, name):
        self.driver.find_element(*self.last_name).send_keys(name)

    def enter_password(self, pwd):
        self.driver.find_element(*self.password).send_keys(pwd)

    def enter_confirm_password(self, pwd):
        self.driver.find_element(*self.confirm_password).send_keys(pwd)

    def get_email_error(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.email_error)
        ).text.strip()

    otp_input = (By.ID, "otp_input")

    signup_btn = (
        By.XPATH,
        "//button[.//span[text()='Sign Up']]"
    )

    verify_btn = (
        By.XPATH,
        "//button[.//span[text()='Verify']]"
    )

    role_dropdown = (
        By.CSS_SELECTOR,
        "select[ng-model='formData.role']"
    )

    joining_year = (By.NAME, "yoj")

    graduation_year = (By.NAME, "yop")

    terms_checkbox = (
        By.XPATH,
        "(//label[contains(@class,'mdl-checkbox')])[1]"
    )

    privacy_checkbox = (
        By.XPATH,
        "(//label[contains(@class,'mdl-checkbox')])[2]"
    )

    join_btn = (
        By.XPATH,
        "//button[.//span[text()='Join Alumni Network']]"
    )

    def click_signup(self):
        self.wait.until(
            EC.element_to_be_clickable(self.signup_btn)
        ).click()

    def enter_otp(self, otp):
        self.wait.until(
            EC.visibility_of_element_located(self.otp_input)
        ).send_keys(otp)


    def click_verify(self):
        self.wait.until(
            EC.element_to_be_clickable(self.verify_btn)
        ).click()


    def select_role(self):
        Select(
            self.wait.until(
                EC.element_to_be_clickable(self.role_dropdown)
            )
        ).select_by_visible_text("Alumni (Past Student)")


    def select_joining_year(self, year):
        Select(
            self.wait.until(
                EC.element_to_be_clickable(self.joining_year)
            )
        ).select_by_visible_text(str(year))


    def select_graduation_year(self, year):
        Select(
            self.wait.until(
                EC.element_to_be_clickable(self.graduation_year)
            )
        ).select_by_visible_text(str(year))


    def accept_terms(self):
        self.wait.until(
            EC.element_to_be_clickable(self.terms_checkbox)
        ).click()


    def accept_privacy(self):
        self.wait.until(
            EC.element_to_be_clickable(self.privacy_checkbox)
        ).click()


    def click_join(self):
        self.wait.until(
            EC.element_to_be_clickable(self.join_btn)
        ).click()