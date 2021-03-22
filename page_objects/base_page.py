import logging

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    elements = {}

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug(f"Create instance of class {self.logger.name}")

    def go_to(self, url):
        self.driver.get(url)
        return self

    def is_title(self, text, wait=5):
        wait = WebDriverWait(self.driver, wait)
        wait.until(EC.title_is(text))
        return self

    def is_element_visible(self, element, wait=5):
        wait = WebDriverWait(self.driver, wait)
        return wait.until(EC.visibility_of_element_located(element))

    def is_all_element_visible(self, wait=5):
        for element in self.elements.values():
            try:
                self.is_element_visible(element, wait)
            except WebDriverException:
                raise AssertionError(element)

    def is_element_clickable(self, element, wait=5):
        wait = WebDriverWait(self.driver, wait)
        return wait.until(EC.element_to_be_clickable(element))
