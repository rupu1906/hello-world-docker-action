from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver import DesiredCapabilities


class DriverExtensions:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_browser_driver(browser, web_config):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            if web_config["headless_mode"] is True:
                options.add_argument("--headless")
            chrome_driver = webdriver.Chrome(
                executable_path=ChromeDriverManager().install(),
                options=options,
            )
            return chrome_driver
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            if web_config["headless_mode"] is True:
                options.headless = True
            firefox_driver = webdriver.Chrome(
                executable_path=GeckoDriverManager().install(), options=options
            )
            return firefox_driver
        elif browser == "edge":
            options = webdriver.EdgeOptions()
            options.use_chromium = True
            if web_config["headless_mode"] is True:
                options.headless = True
            edge_driver = webdriver.Chrome(
                executable_path=EdgeChromiumDriverManager().install(),
                options=options,
            )
            return edge_driver
        return chrome_driver

    @staticmethod
    def get_remote_browser(browser):
        if browser == "egde":
            caps = DesiredCapabilities.EDGE
        elif browser == "firefox":
            caps = DesiredCapabilities.FIREFOX
        else:
            caps = DesiredCapabilities.CHROME
        return caps
