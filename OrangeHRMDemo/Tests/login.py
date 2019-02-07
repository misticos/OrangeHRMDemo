from selenium import webdriver
from OrangeHRMDemo.Pages import loginPage
from OrangeHRMDemo.Pages import welcomePage
import unittest


class LoginTest(unittest.TestCase):

    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="C:/Users/smarkov/PycharmProjects/OrangeHRM/OrangeHRMDemo/drivers")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):

        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_xpath("//*")

# https://opensource-demo.orangehrmlive.com/
# https://www.youtube.com/watch?v=BURK7wMcCwU