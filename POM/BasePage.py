import time

from selenium.webdriver.common.keys import Keys

from Utilities import CustomWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        CustomWait.wait(self.driver, 'click', by_locator).click()

    def presenceOfElement(self, by_locator):
        return CustomWait.wait(self.driver, 'presence', by_locator)

    def clearAndType(self, by_locator, value, keyPress=None):
        ele = CustomWait.wait(self.driver, 'presence', by_locator)
        ele.clear()
        if keyPress is None:
            ele.send_keys(value)
        else:
            ele.send_keys(value, keyPress)

    def type(self, by_locator, value, keyPress=None):
        time.sleep(1)
        ele = CustomWait.wait(self.driver, 'presence', by_locator)
        if keyPress is None:
            ele.send_keys(value)
        else:
            ele.send_keys(value, keyPress)
        time.sleep(1)

    def getText(self, by_locator):
        time.sleep(1)
        ele = CustomWait.wait(self.driver, 'presence', by_locator)
        time.sleep(1)
        return ele.text

    def check_text_presence(self, by_locator, text):
        ele = CustomWait.wait(self.driver, 'text', by_locator, text)
        return ele

    def type_and_enter(self, by_locator, value):
        ele = CustomWait.wait(self.driver, 'presence', by_locator)
        ele.clear()
        ele.send_keys(value, Keys.ENTER)