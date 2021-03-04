from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    elements = {
        "add_to_cart_btn": (By.CSS_SELECTOR, "button#button-cart"),
        "compare_btn": (By.CSS_SELECTOR, 'button[data-original-title="Compare this Product"]'),
        "wishlist_btn": (By.CSS_SELECTOR, "button[data-original-title='Add to Wish List']"),
        "review_btn": (By.CSS_SELECTOR, 'a[href="#tab-review"]'),
        "description_btn": (By.CSS_SELECTOR, 'a[href="#tab-description"]')
    }
