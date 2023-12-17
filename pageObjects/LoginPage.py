from selenium.common import NoSuchElementException, NoAlertPresentException, TimeoutException, \
    ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    Text_Email_XPATH = (By.NAME, "email")
    Text_Password_XPATH = (By.XPATH, "//input[@name='password']")
    Click_Login_XPATH = (By.XPATH, "//span[normalize-space()='Login']")
    Click_Menu_XPATH = (By.CSS_SELECTOR, "button[id='dropdownMenuProfile'] i[class='material-icons']")
    Click_Logout_XPATH = (By.XPATH, "//div[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=0.1)

    def EnterEmail(self, email):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Email_XPATH))
        self.driver.find_element(*LoginPage.Text_Email_XPATH).clear()
        self.driver.find_element(*LoginPage.Text_Email_XPATH).send_keys(email)

    def EnterPassword(self, password):
        self.driver.find_element(*LoginPage.Text_Password_XPATH).clear()
        self.driver.find_element(*LoginPage.Text_Password_XPATH).send_keys(password)

    def ClickLogin(self):
        self.driver.find_element(*LoginPage.Click_Login_XPATH).click()

    def ClickMenu(self):
        wait = WebDriverWait(self.driver, 5)
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.Click_Menu_XPATH))
            self.driver.find_element(*LoginPage.Click_Menu_XPATH).click()
        except ElementClickInterceptedException:
            pass


    def ClickLogout(self):
        wait = WebDriverWait(self.driver, 5)
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.Click_Menu_XPATH))
            self.driver.find_element(*LoginPage.Click_Logout_XPATH).click()
        except ElementNotInteractableException:
            pass


    def Title(self):
        wait = WebDriverWait(self.driver, 5)
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.Click_Menu_XPATH))
            title = self.driver.title
        except TimeoutException:
            title = self.driver.title
        return title

    def Alert(self):
        wait = WebDriverWait(self.driver, 5, poll_frequency=1)
        try:
            print(Alert(self.driver).text)
            alert = Alert(self.driver)
            alert.accept()
        except NoAlertPresentException:
            title = self.driver.title
