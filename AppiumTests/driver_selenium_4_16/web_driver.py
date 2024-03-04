import os
from time import sleep

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Web.config import env
from Web.definitions import BROWSER, LANGUAGE, LOCALE_CODE

browsers = {"chrome": webdriver.Chrome, "remote": webdriver.Remote}

EXPORT_RESULT_IN_TESTRAIL = env.get("EXPORT_RESULT_IN_TESTRAIL", True)
RUN_ID = env.get("PLAN_ID", 0)
CREATE_ALLURE_REPORT = env.get("CREATE_ALLURE_REPORT", True)
ALLURE_REPORT_PATH = env.get("ALLURE_REPORT_PATH", os.path.dirname(__file__))
SESSION_RESULT_PATH = env.get("SESSION_RESULT_PATH", os.path.dirname(__file__))


class Driver:
    def __init__(self, browser_service=None):
        self.options = webdriver.ChromeOptions()
        self.browser_service = browser_service

        if BROWSER == "chrome":
            # ua = UserAgent(fallback="Your favorite Browser")
            # user_agent = ua.random
            self.options.add_argument("--window-size=1920,1080")
            # If you don't want the Chrome browser to display, add the parameter "--headless"
            self.options.add_argument("--headless")
            # options.add_argument(f"--user-agent={user_agent}")
            self.options.add_experimental_option("prefs", {"intl.accept_languages": LOCALE_CODE[LANGUAGE]})
            self.browser_service = Service(ChromeDriverManager().install())

        if BROWSER == "remote":
            print(BROWSER)
            ua = UserAgent(fallback="Your favorite Browser")
            user_agent = ua.random
            self.options.add_argument("--no-sandbox")
            self.options.add_argument("--disable-dev-shm-usage")
            self.options.add_argument("--window-size=1920,1080")
            self.options.add_argument(f"--user-agent={user_agent}")
            self.options.add_experimental_option("prefs", {"intl.accept_languages": LOCALE_CODE[LANGUAGE]})
            self.remote_url = "http://selenium:4444/wd/hub"


    def start(self):
        if BROWSER == "chrome":
            driver = browsers[BROWSER](service=self.browser_service, options=self.options)
        else:
            driver = browsers[BROWSER](command_executor=self.remote_url, options=self.options)
        return driver
        # driver.get('https://www.google.com')
        # print(driver.title)
        # sec = 5
        # for num in range(5):
        #     print(sec)
        #     sec -= 1
        #     sleep(1)
        # driver.quit()


        # return driver

web_driver = Driver()
web_driver.start()


@pytest.fixture(scope="function", autouse=True)
def setup_browser(session):
    try:
        ui_driver = driver_setup.Driver().start()
    except selenium.common.exceptions.SessionNotCreatedException:
        sleep(1)
        ui_driver = driver_setup.Driver().start()
    browser.config.timeout = 2
    browser.config.driver = ui_driver
    session["browser_windows"] = {
        "main_window_handle": browser.driver.current_window_handle,
        "window_handles": browser.driver.window_handles,
    }
    yield
    try:
        browser.config.driver.quit()
    except WebDriverException:
        print("Driver is already closed")