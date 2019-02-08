class LoginPage:

    def __init__(self, driver):
        # Initialize all here. Like driver and locators
        self.driver = driver

        self.login_input         = "//input[@name='txtUsername']"
        self.password_textbox    = "//input[@name='txtPassword']"
        self.login_button        = "//input[@id='btnLogin']"

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.login_input).clear
        self.driver.find_element_by_xpath(self.login_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox).clear
        self.driver.find_element_by_xpath(self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button).click()
