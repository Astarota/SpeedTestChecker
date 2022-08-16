from .pages.base_page import BasePage
from .pages.speed_page import SpeedPage
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
def test_speed_test(browser):
  link="https://www.speedtest.net/"
  for i in range(2,7):
    page=SpeedPage(browser,link)
    page.open()
    page.should_be_go_click()
    page.should_be_close_button()
    page.should_be_close_window()
    page.should_be_download_number()
    page.should_be_upload_number()
    page.should_be_putted_in_excel_download_number(i)
    page.should_be_putted_in_excel_upload_number(i)
    i=i+1