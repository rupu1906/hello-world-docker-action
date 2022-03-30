import time
import unittest
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import DesiredCapabilities
import os

class HackerNewsSearchTest(unittest.TestCase):

    def setUp(self):
        load_dotenv()
        browser_name = os.environ.get("BROWSER")
        
        if browser_name =="firfox":
            caps = DesiredCapabilities.FIREFOX
        else:
            caps = DesiredCapabilities.CHROME
        self.browser = webdriver.Remote(
            command_executor=f"http://localhost:4444/wd/hub", 
            desired_capabilities= caps
        )

    def test_hackernews_search_for_testdrivenio(self):
        browser = self.browser
        load_dotenv()
        url = os.environ.get("URL")
        browser.get(url)
        print(browser.title)
        search_box = browser.find_element(By.NAME, 'q')
        search_box.send_keys('testdriven.io')
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)  # simulate long running test
        self.assertIn('testdriven.io', browser.page_source)

    def test_hackernews_search_for_selenium(self):
        load_dotenv()
        browser = self.browser
        url = os.environ.get("URL")
        browser.get(url)
        search_box = browser.find_element(By.NAME, 'q')
        search_box.send_keys('selenium')
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)  # simulate long running test
        self.assertIn('selenium', browser.page_source)

    def test_hackernews_search_for_testdriven(self):
        load_dotenv()
        browser = self.browser
        url = os.environ.get("URL")
        browser.get(url)
        search_box = browser.find_element(By.NAME, 'q')
        search_box.send_keys('testdriven')
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)  # simulate long running test
        self.assertIn('testdriven', browser.page_source)

    def test_hackernews_search_with_no_results(self):
        load_dotenv()
        browser = self.browser
        url = os.environ.get("URL")
        browser.get(url)
        search_box = browser.find_element(By.NAME, 'q')
        search_box.send_keys('?*^^%')
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)  # simulate long running test
        self.assertNotIn('<em>', browser.page_source)

    def tearDown(self):
        self.browser.quit()  # quit vs close?


if __name__ == '__main__':
    unittest.main()