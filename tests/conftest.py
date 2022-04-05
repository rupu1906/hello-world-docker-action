import pytest
from configuration_reader import ConfigurationReader
from driver import DriverExtensions
from selenium import webdriver


config = ConfigurationReader()
platform_config = config.read_json("src/PracticeTests", "config.json")
web_config = platform_config.get("Web")

def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="ios")
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--remote", action="store_true", default="False")
    parser.addoption("--host", action="store", default="127.0.0.1", type=str)
    parser.addoption("--port", action="store", default="4444", type=int)
    parser.addoption("--locale", action="store", default="en_ca")
    parser.addoption(
        "--log-disable", action="append", default=[], help="ex: debug,info...."
    )

@pytest.fixture(name="browser")
def fixture_browser(request):
    cli_request = request.config.getoption("browser").lower()
    if cli_request not in web_config["supported_browsers"]:
        raise Exception(f'"{cli_request}" is not a supported browser')
    return cli_request


@pytest.fixture(name="locale")
def fixture_locale(request):
    locale = request.config.getoption("locale")
    if locale not in web_config["supported_locale"]:
        raise Exception(f'"{locale}" is not a supported locale')
    return locale


@pytest.fixture
def web_setup(request, browser):
    host = request.config.getoption("--host")
    port = request.config.getoption("--port")
    caps = request.config.getoption("--browser")
    if request.config.getoption("--remote") != "False":
        driver = webdriver.Remote(
            f"http://{host}:{port}/wd/hub",
            desired_capabilities=DriverExtensions.get_remote_browser(caps),
        )
    else:
        driver = DriverExtensions.get_browser_driver(browser, web_config)
        driver.maximize_window()
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    yield driver
    if request.session.testsfailed != before_failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Test failed",
            attachment_type=AttachmentType.PNG,
        )
    driver.quit()
