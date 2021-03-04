from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    elements = {
        "email_input": (By.CSS_SELECTOR, "input[name='email']"),
        "password_input": (By.CSS_SELECTOR, "input[name='password']"),
        "login_submit_btn": (By.CSS_SELECTOR, "input[value='Login']"),
        "continue_register_btn": (By.CSS_SELECTOR, "div.well > a.btn"),
        "forgotten_password_btn": (By.CSS_SELECTOR, "div.well > form > div.form-group > a")
    }
