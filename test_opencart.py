import uuid
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from page_objects import MainPage, CategoryPage, ProductPage, LoginPage, AdminLoginPage, \
                         AdminDashboardPage


class TestFirstTask:

    def test_main_page_title(self, browser, endpoint):
        MainPage(browser) \
            .go_to(endpoint['main']) \
            .is_title('Your Store')


class TestSecondTask:

    def test_main_page_element_visibility(self, browser):
        MainPage(browser) \
            .is_all_element_visible()

    def test_products_page_element_visibility(self, browser, endpoint):
        CategoryPage(browser) \
            .go_to(endpoint['products']) \
            .is_all_element_visible()

    def test_galaxy_tab_page_element_visibility(self, browser, endpoint):
        ProductPage(browser) \
            .go_to(endpoint['galaxy_tab']) \
            .is_all_element_visible()

    def test_login_page_element_visibility(self, browser, endpoint):
        LoginPage(browser) \
            .go_to(endpoint['login']) \
            .is_all_element_visible()

    def test_admin_page_element_visibility(self, browser, endpoint):
        AdminLoginPage(browser) \
            .go_to(endpoint['admin_login']) \
            .is_all_element_visible()


class TestThirdTask:
    category_name = None

    def test_login_admin_panel(self, browser, credentials):
        AdminLoginPage(browser) \
            .login_with(credentials["admin"]) \
            .is_title("Dashboard")

    def test_fault_create_invalid_categories(self, browser):
        AdminDashboardPage(browser)
        wait = WebDriverWait(browser, 5)

        catalog_menu = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-toggle='collapse'] > i.fa-tags")))
        catalog_menu.click()
        category_section = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='collapse1']/li[1]/a")))
        category_section.click()
        add_new_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-original-title='Add New']")))
        add_new_btn.click()
        save_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-original-title='Save']")))
        save_btn.click()

        error_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.alert-danger")))
        assert error_message.text == "Warning: Please check the form carefully for errors!\n×"

    def test_create_valid_categories(self, browser):
        wait = WebDriverWait(browser, 5)
        name_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder = 'Category Name']")))
        self.category_name = str(uuid.uuid4())  # сохраняю имя новой категории для ассерта
        name_field.send_keys(self.category_name)
        tag_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Meta Tag Title']")))
        tag_field.send_keys("Testy test")
        save_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-original-title='Save']")))
        save_btn.click()

        assert wait.until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{self.category_name}')]")))

    def test_logout_admin_panel(self, browser):
        wait = WebDriverWait(browser, 5)
        logout_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "i.fa-sign-out")))
        logout_btn.click()
        login_form_header = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.panel-title")))
        assert login_form_header.text == "Please enter your login details."
