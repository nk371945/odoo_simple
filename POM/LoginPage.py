from selenium.webdriver.common.by import By

from POM.AppListPage import AppListPage
from POM.BasePage import BasePage


class LoginPage(BasePage):
    USERNAME = (By.XPATH, "//input[@placeholder='Email']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BTN = (By.XPATH, "//button[text()='Log in']")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def enterUserName(self, username):
        self.clearAndType(self.USERNAME, username)

    def enterPassword(self, password):
        self.clearAndType(self.PASSWORD, password)

    def login(self):
        self.click(self.LOGIN_BTN)
        return AppListPage(self.driver)
