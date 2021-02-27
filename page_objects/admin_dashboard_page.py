from selenium.webdriver.common.by import By
from .base_page import BasePage


class AdminDashboardPage(BasePage):
    elements = {
        "logo": (By.CSS_SELECTOR, "div.navbar-header > a"),
        "password_input": (By.CSS_SELECTOR, "input[name='password']"),
        "name_input": (By.CSS_SELECTOR, "input[name='username']"),
        "login_submit_btn": (By.CSS_SELECTOR, "div.text-right > button"),
        "forgotten_password_btn": (By.CSS_SELECTOR, "div.form-group > span > a")
    }

