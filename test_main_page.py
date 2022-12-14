from selenium.webdriver.support.ui import WebDriverWait
from pages.speed_page import SpeedPage
import time
import pytest
def test_speed_test(browser):
  link="https://www.speedtest.net/"
  for i in range(2,7):
    page=SpeedPage(browser,link)
    page.open()
    page.should_be_go_click()
    page.should_be_close_window()
    page.should_be_putted_in_excel_download_number(i)
    page.should_be_putted_in_excel_upload_number(i)
    i=i+1