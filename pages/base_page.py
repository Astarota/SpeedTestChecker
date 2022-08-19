from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import openpyxl as O

class BasePage():

    def __init__(self, browser, url, timeout=2):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        
    def open(self):
        try:
            self.browser.get(self.url)
        except(WebDriverException):
            for i in range(2,7):
                wb=O.load_workbook(Excel_file)
                ws=wb[Excel_worksheet]
                ws.cell(i,i).value=download_number.text
                wb.save(Excel_file)
                wb.close()


    def is_element_present(self, how, what, timeout=30):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except (NoSuchElementException):
            return False
        return True
    #Проверка если элемент представлен
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):  # проверяем что элемент исчезает в течении времени
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True