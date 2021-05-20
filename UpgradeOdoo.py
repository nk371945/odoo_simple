import ctypes
import os
import sys
import time

from selenium import webdriver

from POM.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    # Code of your program here
    cmd1 = ' net stop "postgresql-x64-13"  '
    cmd2 = ' net start "postgresql-x64-13"  '
    os.popen(cmd1)
    time.sleep(5)
    os.popen(cmd2)
    time.sleep(5)
    browser = sys.argv[1]
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()

    driver.get(ReadConfig.getApplicationURL())
    lp = LoginPage(driver)

    lp.enterUserName(ReadConfig.getUsername())
    lp.enterPassword(ReadConfig.getPassword())
    alp = lp.login()

    alp.clickMenu()
    alp.selectApps()
    time.sleep(3)
    alp.upgradeApp()

    # alp.logout()
    driver.quit()

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
