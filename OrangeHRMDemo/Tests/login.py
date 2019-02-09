from selenium import webdriver
from OrangeHRMDemo.Pages.BaseTestPage import BaseTestPage
import unittest


class LoginTest(unittest.TestCase, BaseTestPage):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        self.driver.implicitly_wait(100)
        self.driver.maximize_window()

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        self.login_page.enter_username("Admin")
        self.login_page.enter_password("admin123")
        self.login_page.click_login()

        self.welcome_page.click_welcome()
        self.welcome_page.click_logout()

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completed")
