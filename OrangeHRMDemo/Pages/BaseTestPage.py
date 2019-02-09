from OrangeHRMDemo.Pages.loginPage import LoginPage
from OrangeHRMDemo.Pages.welcomePage import WelcomePage


class BaseTestPage(object):

    def __init__(self, driver):
        self.driver = driver

    @property
    def login_page(self):
        return LoginPage(self.driver)

    @property
    def welcome_page(self):
        return WelcomePage(self.driver)


