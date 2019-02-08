from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class WelcomePage:

    def __init__(self, driver):
        # Initialize all here. Like driver and locators
        self.driver = driver

        self.welcome_admin_button = "//*[@id='welcome']"
        self.logout = "//*[contains(text(), 'Logout')]"

    def click_welcome(self):

        self.driver.find_element_by_xpath(self.welcome_admin_button).click()

    def click_logout(self):

        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.logout))
            )
        finally:
            self.driver.find_element_by_xpath(self.logout).click()
