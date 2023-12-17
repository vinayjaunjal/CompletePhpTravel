import time

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert

from pageObjects.LoginPage import LoginPage
from utilities.Logger import LogGenerator
from utilities.ReadConfig import Readconfig


class Test_Login_Params:
    url = Readconfig.URL()
    email = Readconfig.Email()
    password = Readconfig.Password()
    log = LogGenerator.loggen()

    def test_login_Params_003(self, setup, getDataforlogin):
        self.log.info("test_login_Params_003 is started")
        self.driver = setup
        self.log.info("Opening Browser")
        self.lp = LoginPage(self.driver)
        self.driver.get(self.url)
        self.log.info("Going to Url -->" + str(self.url))
        self.lp = LoginPage(self.driver)
        self.lp.EnterEmail(getDataforlogin[0])
        self.log.info("Entering Email-->" + str(getDataforlogin[0]))
        self.lp.EnterPassword(getDataforlogin[1])
        self.log.info("Entering Password-->" + getDataforlogin[1])
        self.lp.ClickLogin()
        self.log.info("Clicking Login")
        self.lp.Alert()

        statusList = []
        if self.lp.Title() == "Dashboard":
            if getDataforlogin[2] == "Pass":
                self.log.info("Page Title -->" + self.driver.title)
                self.lp.ClickMenu()
                self.log.info("Clicking Menu Button")
                self.driver.save_screenshot(
                    "C:\\Users\\HP\\PycharmProjects\\CompletePhpTravel\\Screenshots"
                    "\\" + getDataforlogin[0] + getDataforlogin[0] + "test_login_Params_003_pass.PNG")
                # time.sleep(2)
                self.lp.ClickLogout()
                self.log.info("Clicking Logout Button")
                statusList.append("Pass")

            elif getDataforlogin[2] == "Fail":
                self.log.info("Page Title -->" + self.driver.title)
                self.lp.ClickMenu()
                self.log.info("Clicking Menu Button")
                self.driver.save_screenshot(
                    "C:\\Users\\HP\\PycharmProjects\\CompletePhpTravel\\Screenshots"
                    "\\" + getDataforlogin[0] + getDataforlogin[0] + "test_login_Params_003_fail.PNG")
                # time.sleep(2)
                self.lp.ClickLogout()
                self.log.info("Clicking Logout Button")
                statusList.append("Fail")

        else:
            if getDataforlogin[2] == "Pass":
                self.log.info("Page Title -->" + self.driver.title)
                self.driver.save_screenshot(
                    "C:\\Users\\HP\\PycharmProjects\\CompletePhpTravel\\Screenshots"
                    "\\" + getDataforlogin[0] + getDataforlogin[0] + "test_login_Params_003_fail.PNG")
                statusList.append("Fail")

            elif getDataforlogin[2] == "Fail":
                self.log.info("Page Title -->" + self.driver.title)
                self.driver.save_screenshot(
                    "C:\\Users\\HP\\PycharmProjects\\CompletePhpTravel\\Screenshots"
                    "\\" + getDataforlogin[0] + getDataforlogin[0] + "test_login_Params_003_pass.PNG")
                statusList.append("Pass")

        if "Fail" not in statusList:
            assert True
            self.log.info("test_login_Params_003 is Passed")
        else:
            assert False
            self.log.info("test_login_Params_003 is Failed")
        self.log.info("test_login_Params_003 is Completed")
