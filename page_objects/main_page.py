from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    elements = {
        "search_box": (By.CSS_SELECTOR, "input[name='search']"),
        "cart_icon": (By.CSS_SELECTOR, "span#cart-total"),
        "navbar_header": (By.CSS_SELECTOR, "div.navbar-header"),
        "add_cart_button": (By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[3]/button[1]'),
        "info_header": (By.CSS_SELECTOR, "div.row > div.col-sm-3 > h5")
    }
