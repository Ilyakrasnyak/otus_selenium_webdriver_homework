from selenium.webdriver.common.by import By

from ..base_page import BasePage


class AdminDashboardMenu(BasePage):

    elements = {
        "catalog_menu": (By.CSS_SELECTOR, "[data-toggle='collapse'] > i.fa-tags"),
        "category_section": (By.XPATH, "//*[@id='collapse1']/li[1]/a")
    }

    def open_categories(self, wait=5):
        self.is_element_clickable(self.elements['catalog_menu'], wait).click()
        self.is_element_clickable(self.elements['category_section'], wait).click()
        return self

