import pytest
from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions
from selenium.webdriver.support.ui import WebDriverWait


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera"],
                     default='chrome', help="Browser")
    parser.addoption("--host", action="store", default="127.0.0.1", help="Base URL")


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("--browser")

    driver = None

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        # options.headless = True
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)

    elif browser == "opera":
        options = OperaOptions()
        options.headless = True
        driver = webdriver.Opera(options=options)

    driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def endpoint(request):
    host = "http://" + request.config.getoption("--host")
    endpoint = {
        "main": host,
        "products": host + "/index.php?route=product/category&path=20",
        "galaxy_tab": host + "/index.php?route=product/product&path=57&product_id=49",
        "login": host + "/index.php?route=account/login",
        "register": host + "/index.php?route=account/register",
        "pass_recovery": host + "/index.php?route=account/forgotten",
        "admin": host + "/admin/"
    }
    return endpoint


@pytest.fixture(scope="session")
def admin():
    admin = {
        "name": "user",
        "password": "bitnami"
    }
    return admin
