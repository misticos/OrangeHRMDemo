from selenium import webdriver
import time
from OrangeHRMDemo.Pages import loginPage
from OrangeHRMDemo.Pages import welcomePage
import unittest


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def test_login(self):

        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_xpath("//*")


# if __name__ == "__main__": unittest.main()

# https://opensource-demo.orangehrmlive.com/
# https://www.youtube.com/watch?v=BURK7wMcCwU