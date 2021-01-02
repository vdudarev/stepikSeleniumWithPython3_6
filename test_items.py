import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
cssSelector = "button.btn-add-to-basket"

def test_checkAddToBasketButtonExistance(browser):
    browser.get(link)
    #time.sleep(30)
    button = None
    try:
        button = WebDriverWait(browser, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, cssSelector))
        )
    except Exception as err:
        print("Exception: {0}".format(err))
    assert button != None, "Add-to-basket button not found"
