import time

from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.LoginPage import LoginPage
from utilities.Logger import LogGenerator
from utilities.ReadConfig import Readconfig

class Test_Login:
    url = Readconfig.URL()
    email = Readconfig.Email()
    password = Readconfig.Password()
    log = LogGenerator.loggen()

    def test_page_title_001(self, setup):
        self.log.info("test_page_title_001 is started")
        self.driver = setup
        self.log.info("Opening Browser")
        self.lp = LoginPage(self.driver)
        self.driver.get(self.url)
        self.log.info("Going to Url -->" + self.url)
        if self.driver.title == "Administator Login":
            self.log.info("Page Title -->" + self.driver.title)
            self.driver.save_screenshot(
                "C:\\Users\\HP\\PycharmProjects\\CompletePhpTravel\\Screenshots"
                "\\test_page_title_001_pass.PNG")
            assert True
            self.log.info("test_page_title_001 is Passed")
        else:
            self.log.info("Page Title -->" + self.driver.title)
            self.log.info("test_page_title_001 is Failed")
            self.driver.save_screenshot(
                "C:\\Users\\HP\\PycharmProjects\\CompletePhpTravel\\Screenshots"
                "\\test_page_title_001_fail.PNG")
            assert False
        self.log.info("test_page_title_001 is Completed")

    def test_login_002(self, setup):
        self.log.info("test_login_002 is started")
        self.driver = setup
        self.log.info("Opening Browser")
        self.lp = LoginPage(self.driver)
        self.driver.get(self.url)
        self.log.info("Going to Url -->" + str(self.url))
        self.lp = LoginPage(self.driver)
        time.sleep(2)
        self.lp.EnterEmail(self.email)
        self.log.info("Entering Email-->" + str(self.email))
        self.lp.EnterPassword(self.password)
        self.log.info("Entering Password-->" + self.password)
        self.lp.ClickLogin()
        self.log.info("Clicking Login")
        time.sleep(2)
        wait = WebDriverWait(self.driver, 15, poll_frequency=1)
        try:
            wait.until(expected_conditions.visibility_of_element_located((self.lp.Click_Menu_XPATH)))
            title = self.driver.title
        except NoSuchElementException:
            title = self.driver.title

        if self.lp.Title == True:
            self.log.info("Page Title -->" + self.driver.title)
            time.sleep(10)
            self.lp.ClickMenu()
            self.log.info("Clicking Menu Button")
            self.driver.save_screenshot(
                "C:\\Users\\HP\\PycharmProjects\\CompletePhpTravel\\Screenshots"
                "\\test_login_002_pass.PNG")
            self.lp.ClickLogout()
            self.log.info("Clicking Logout Button")
            assert True
            self.log.info("test_login_002 is Passed")
        else:
            self.log.info("Page Title -->" + self.driver.title)
            self.driver.save_screenshot(
                "C:\\Users\\HP\\PycharmProjects\\CompletePhpTravel\\Screenshots"
                "\\test_login_002_fail.PNG")
            assert False
            self.log.info("test_login_002 is Failed")
        self.log.info("test_login_002 is Completed")
