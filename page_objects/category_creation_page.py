from selenium.webdriver.common.by import By
from .base_page import BasePage


class CategoryCreationPage(BasePage):
    elements = {
        "save_button": (By.CSS_SELECTOR, "button[data-original-title='Save']"),
        "name_field" : (By.CSS_SELECTOR, "input[placeholder = 'Category Name']"),
        "meta_tag_field": (By.CSS_SELECTOR, "input[placeholder='Meta Tag Title']")
    }

    arising_elements = {
        "creating_alert": (By.CSS_SELECTOR, "div.alert-danger")
    }

    def save_category(self):
        self.is_element_clickable(self.elements["save_button"]).click()
        return self

    def take_error_with_text(self, text):
        error_message = self.is_element_visible(self.arising_elements["creating_alert"])
        assert error_message.text == text

    def fill_category_name(self, text):
        self.is_element_clickable(self.elements["name_field"]).send_keys(text)
        return self

    def fill_tag_title(self, text):
        self.is_element_clickable(self.elements["meta_tag_field"]).send_keys(text)
        return self
