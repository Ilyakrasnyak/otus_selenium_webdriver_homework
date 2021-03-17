import logging

import pytest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

logging.basicConfig(level="INFO", filename="logs/journal.log",
                    format='%(asctime)s - %(name)s:%(levelname)s - %(message)s')


class MyListener(AbstractEventListener):
    logger = logging.getLogger("DriverEvent")

    def before_navigate_to(self, url, driver):
        self.logger.info(f"I'm navigating to {url}")

    def on_exception(self, exception, driver):
        self.logger.error(f'Selenium exception: {exception}')
        driver.save_screenshot(f'logs/screenshots/{exception}.png')


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera"],
                     default='chrome', help="Browser")
    parser.addoption("--host", action="store", default="192.168.0.4", help="Base URL")
    parser.addoption("--executor", action="store", default="192.168.0.4")
    parser.addoption("--bversion", action="store", default="88.0")
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--videos", action="store_true", default=False)


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")

    executor_url = f"http://{executor}:4444/wd/hub"

    caps = {
        "browserName": browser,
        "browserVersion": version,
        "screenResolution": "1280x720",
        "selenoid:options": {
            "enableVNC": vnc,
            "enableVideo": videos,
            "enableLog": logs
        }
    }

    driver = webdriver.Remote(
        command_executor=executor_url,
        desired_capabilities=caps
    )

    driver.maximize_window()
    driver = EventFiringWebDriver(driver, MyListener())
    logging.info(f"Start session with {driver.name}")

    yield driver

    logging.info(f"End session with {driver.name}")
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
        "admin_login": host + "/admin/"
    }
    return endpoint


@pytest.fixture(scope="session")
def credentials():
    credentials = {
        "admin": ("user", "bitnami"),
        "error_auth": ("permanent", "fault")
    }
    return credentials
