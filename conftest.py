from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest

@pytest.fixture(scope="function")
def browser():
    caps = DesiredCapabilities().CHROME
    #caps["pageLoadStrategy"] = "normal"  #  complete
    #caps["pageLoadStrategy"] = "eager"  #  interactive
    caps["pageLoadStrategy"] = "none"
    browser = webdriver.Chrome(desired_capabilities=caps, executable_path=r'C:\chromedriver\chromedriver.exe')
    option = webdriver.ChromeOptions()
    option.add_argument("--log-level=3")
    option.add_argument("--ignore-certificate-errors")
    option.add_argument("--ignore-ssl-errors")
    #option.add_argument("--headless")
    option.add_argument("--disable-gpu")
    option.add_argument("--disable-software-rasterizer")
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=option)
    yield browser
    print("\nquit browser..")
    browser.quit()