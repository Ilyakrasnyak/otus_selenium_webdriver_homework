from .base_page import BasePage
from selenium.webdriver.common.by import By


class AdminCategoryPage(BasePage):

    elements = {
        "add_new_btn": (By.CSS_SELECTOR, "a[data-original-title='Add New']"),
        "rebuild_btn": (By.CSS_SELECTOR, "a[data-original-title='Rebuild']"),
        "delete_btn": (By.CSS_SELECTOR, "a[data-original-title='Delete']"),
        "column_title_name": (By.CSS_SELECTOR, "thead td.text-left"),
        "column_title_checkmark": (By.CSS_SELECTOR, "thead td.text-center"),
        "logout_btn": (By.CSS_SELECTOR, "i.fa-sign-out")
    }

    def create_new_category(self):
        self.is_element_clickable(self.elements["add_new_btn"]).click()
        return self

    def is_category_exist(self, category_name):
        self.is_element_visible((By.XPATH, f"//*[contains(text(), '{category_name}')]"))
        return self

    def logout(self):
        self.is_element_clickable(self.elements["logout_btn"]).click()
        return self
