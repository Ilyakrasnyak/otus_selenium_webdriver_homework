from selenium.webdriver.common.by import By
from .base_page import BasePage


class AdminLoginPage(BasePage):
    elements = {
        "logo": (By.CSS_SELECTOR, "div.navbar-header > a"),
        "password_input": (By.CSS_SELECTOR, "input[name='password']"),
        "name_input": (By.CSS_SELECTOR, "input[name='username']"),
        "login_submit_btn": (By.CSS_SELECTOR, "div.text-right > button"),
        "forgotten_password_btn": (By.CSS_SELECTOR, "div.form-group > span > a")
    }

    def login_with(self, credentials: tuple, wait=5):
        self.is_element_clickable(self.elements['name_input'], wait).send_keys(credentials[0])
        self.is_element_clickable(self.elements['password_input'], wait).send_keys(credentials[1])
        self.is_element_clickable(self.elements['login_submit_btn'], wait).click()
        return self
