from selenium import webdriver
from OrangeHRMDemo.Pages.loginPage import LoginPage
from OrangeHRMDemo.Pages.welcomePage import WelcomePage
import unittest


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)

        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        welcomepage = WelcomePage(driver)
        welcomepage.click_welcome()
        welcomepage.click_logout()

