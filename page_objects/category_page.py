from .base_page import BasePage
from selenium.webdriver.common.by import By


class CategoryPage(BasePage):

    elements = {
        "phone_icon": (By.CSS_SELECTOR, "i.fa-phone"),
        "user_icon": (By.CSS_SELECTOR, "i.fa-user"),
        "heart_icon": (By.CSS_SELECTOR, "i.fa-heart"),
        "shop_cart_icon": (By.CSS_SELECTOR, "i.fa-shopping-cart"),
        "share_icon": (By.CSS_SELECTOR, "i.fa-share")
    }