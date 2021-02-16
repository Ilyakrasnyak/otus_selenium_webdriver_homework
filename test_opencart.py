import time
from selenium.common.exceptions import WebDriverException


class TestFirstTask:
    """Тест, который открывает основную страницу opencart и проверяет,
     что мы находимся именно на странице приложения opencart."""

    def test_main_page_title(self, browser, endpoint):
        browser.get(endpoint['main'])
        assert browser.title == 'Your Store'


class TestSecondTask:
    """Тесты проверяющие наличие элементов
       на разных страницах приложения """

    def test_main_page_element_presence(self, browser, endpoint):
        browser.get(endpoint['main'])
        try:
            browser.find_element_by_css_selector("input[name='search']")
            browser.find_element_by_css_selector("span#cart-total")
            browser.find_element_by_css_selector("div.navbar-header")
            browser.find_element_by_css_selector("img[alt='MacBook']")
            browser.find_element_by_css_selector("div.row > div.col-sm-3 > h5")
        except WebDriverException as e:
            raise AssertionError(e)

    def test_products_page_element_presence(self, browser, endpoint):
        browser.get(endpoint['products'])
        try:
            browser.find_element_by_css_selector("i.fa-phone")
            browser.find_element_by_css_selector("i.fa-user")
            browser.find_element_by_css_selector("i.fa-heart")
            browser.find_element_by_css_selector("i.fa-shopping-cart")
            browser.find_element_by_css_selector("i.fa-share")
        except WebDriverException as e:
            raise AssertionError(e)

    def test_galaxy_tab_page_element_presence(self, browser, endpoint):
        browser.get(endpoint['galaxy_tab'])
        try:
            browser.find_element_by_css_selector("button[data-toggle = 'dropdown'] > strong")
            browser.find_element_by_css_selector("button#button-cart")
            browser.find_element_by_css_selector("i.fa-star-o")
            browser.find_element_by_css_selector("button[data-original-title='Add to Wish List']")
            browser.find_element_by_css_selector("a.thumbnail[title='Samsung Galaxy Tab 10.1']")
        except WebDriverException as e:
            raise AssertionError(e)

    def test_login_page_element_presence(self, browser, endpoint):
        browser.get(endpoint['login'])
        try:
            browser.find_element_by_css_selector(f"div.well > a[href='{endpoint['register']}']")
            browser.find_element_by_css_selector("input[name='email']")
            browser.find_element_by_css_selector("input[name='password']")
            browser.find_element_by_css_selector("input[value='Login']")
            browser.find_element_by_css_selector(f"div.form-group > a[href='{endpoint['pass_recovery']}']")
        except WebDriverException as e:
            raise AssertionError(e)

    def test_admin_page_element_presence(self, browser, endpoint):
        browser.get(endpoint['login'])
        try:
            browser.find_element_by_css_selector(".fa-bars")
            browser.find_element_by_css_selector("input[name='username']")
            browser.find_element_by_css_selector("input[name='password']")
            browser.find_element_by_css_selector("input[value='Login']")
            browser.find_element_by_css_selector(f"div.form-group > a[href='{endpoint['pass_recovery']}']")
        except WebDriverException as e:
            raise AssertionError(e)