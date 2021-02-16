import uuid
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException


class TestFirstTask:

    def test_main_page_title(self, browser, endpoint):
        browser.get(endpoint['main'])
        wait = WebDriverWait(browser, 5)
        assert wait.until(EC.title_is('Your Store'))


class TestSecondTask:

    def test_main_page_element_presence(self, browser, endpoint):
        browser.get(endpoint['main'])
        wait = WebDriverWait(browser, 5)
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='search']")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span#cart-total")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.navbar-header")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[alt='MacBook']")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.row > div.col-sm-3 > h5")))
        except WebDriverException as e:
            raise AssertionError(e)

    def test_products_page_element_presence(self, browser, endpoint):
        browser.get(endpoint['products'])
        wait = WebDriverWait(browser, 5)
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i.fa-phone")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i.fa-user")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i.fa-heart")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i.fa-shopping-cart")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i.fa-share")))
        except WebDriverException as e:
            raise AssertionError(e)

    def test_galaxy_tab_page_element_presence(self, browser, endpoint):
        browser.get(endpoint['galaxy_tab'])
        wait = WebDriverWait(browser, 5)
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-toggle = 'dropdown'] > strong")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button#button-cart")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i.fa-star-o")))
            wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-original-title='Add to Wish List']")))
            wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "a.thumbnail[title='Samsung Galaxy Tab 10.1']")))

        except WebDriverException as e:
            raise AssertionError(e)

    def test_login_page_element_presence(self, browser, endpoint):
        browser.get(endpoint['login'])
        wait = WebDriverWait(browser, 5)
        try:
            wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, f"div.well > a[href='{endpoint['register']}']")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='password']")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='Login']")))
            wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, f"div.form-group > a[href='{endpoint['pass_recovery']}']")))

        except WebDriverException as e:
            raise AssertionError(e)

    def test_admin_page_element_presence(self, browser, endpoint):
        browser.get(endpoint['admin'])
        wait = WebDriverWait(browser, 5)
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[id='header-logo']")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='username']")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='password']")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i.fa-key")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.form-group > span > a")))

        except WebDriverException as e:
            raise AssertionError(e)


class TestThirdTask:
    category_name = None

    def test_login_admin_panel(self, browser, endpoint, admin):
        wait = WebDriverWait(browser, 5)

        username_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        username_field.send_keys(admin["name"])
        pass_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
        pass_field.send_keys(admin["password"])
        submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        submit_btn.click()

        assert wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#navigation")))

    def test_fault_create_invalid_categories(self, browser):
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
