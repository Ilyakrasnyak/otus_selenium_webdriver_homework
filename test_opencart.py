import uuid

from page_objects import MainPage, CategoryPage, ProductPage, LoginPage, AdminLoginPage, \
                         AdminDashboardPage, CategoryCreationPage, AdminCategoryPage


class TestOpenCart:
    category_name = None

    def test_main_page_title(self, browser, endpoint):
        MainPage(browser) \
            .go_to(endpoint['main']) \
            .is_title('Your Store')

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

    def test_login_admin_panel(self, browser, credentials):
        AdminLoginPage(browser) \
            .login_with(credentials["admin"]) \
            .is_title("Dashboard")

    def test_fault_create_invalid_categories(self, browser):
        AdminDashboardPage(browser) \
            .menu.open_categories()
        AdminCategoryPage(browser) \
            .create_new_category()
        CategoryCreationPage(browser) \
            .save_category() \
            .take_error_with_text("Warning: Please check the form carefully for errors!\n×")

    def test_create_valid_categories(self, browser):
        self.category_name = str(uuid.uuid4())  # сохраняю имя новой категории для ассерта
        CategoryCreationPage(browser) \
            .fill_category_name(self.category_name) \
            .fill_tag_title("test_tag") \
            .save_category()
        AdminCategoryPage(browser) \
            .is_category_exist(self.category_name)

    def test_logout_admin_panel(self, browser):
        AdminCategoryPage(browser).logout()
        AdminLoginPage(browser).is_all_element_visible()
