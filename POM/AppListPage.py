import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from POM.BasePage import BasePage
from Utilities.readProperties import ReadConfig


class AppListPage(BasePage):
    MENU = (By.XPATH, "//a[@class='full']")
    APPS = (By.LINK_TEXT, "Apps")
    SEARCH_TAG = (By.XPATH, "//div[@class='o_searchview_facet']")
    UPDATE_APP_LIST = (By.XPATH, "//ul[@class='o_menu_sections']//span[contains(text(),'Update Apps List')]")
    UPDATE_MODULE = (By.NAME, "update_module")
    USER_MENU = (By.CLASS_NAME, "o_user_menu")
    LOGOUT = (By.LINK_TEXT, "Log out")

    SEARCH_INPUT = (By.XPATH, "//input[@accesskey='Q']")
    DROPDOWN_TOGGLE = (By.XPATH, "(//div[@class='o_dropdown_kanban dropdown']//a)[1]")
    UPGRADE = (By.XPATH, "//div[@class='dropdown-menu show']//a[text()='Upgrade']")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def upgradeApp(self):
        if self.driver.find_elements(*self.SEARCH_TAG)[0].is_displayed():
            tagList = self.driver.find_elements(*self.SEARCH_TAG)

            for ele in tagList:
                ele.find_elements_by_xpath("./child::*")[2].click()

        self.type(self.SEARCH_INPUT, ReadConfig.getModuleName(), Keys.ENTER)
        self.click(self.DROPDOWN_TOGGLE)
        self.click(self.UPGRADE)
        time.sleep(15)

    def clickMenu(self):
        self.click(self.MENU)

    def selectApps(self):
        self.click(self.APPS)
        time.sleep(3)

    def clickUpdateAppList(self):
        self.click(self.UPDATE_APP_LIST)

    def clickUpdateModuleBtn(self):
        self.click(self.UPDATE_MODULE)

    def logout(self):
        self.click(self.USER_MENU)
        self.click(self.LOGOUT)

    # def remove_search_tags(self):
