import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    elif browser == 'edge':
        print("Launching Edge Browser")
        driver = webdriver.Edge()
    else:
        print("Headless mode")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()




@pytest.fixture(params=[
    ("admin@phptravels.com", "demoadmin", "Pass"),
    ("admin@phptravels.com1", "demoadmin", "Fail"),
    ("admin@phptravels.com", "demoadmin1", "Fail"),
    ("admin@phptravels.com1", "demoadmin1", "Fail")
])
def getDataforlogin(request):
    return request.param


def pytest_metadata(metadata):
    # To Add
    metadata["Environment"] = "Test"
    metadata['Project Name'] = 'OrangHRM'
    metadata['Module Name'] = 'Employee'
    metadata['Tester'] = 'Credence'
    # Remove
    metadata.pop("Platform", None)
