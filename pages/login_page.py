from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login URL doesn't contain substring 'login'"

    def register_new_user(self, email, password):
        self.browser.find_element(By.ID, "id_registration-email").send_keys(email)
        self.browser.find_element(By.ID, "id_registration-password1").send_keys(password)
        self.browser.find_element(By.ID, "id_registration-password2").send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, '.btn[name = "registration_submit"]').click()

