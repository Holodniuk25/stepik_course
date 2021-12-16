import math
from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    
    browser = webdriver.Chrome()
    browser.get(link)
    btn = browser.find_element_by_css_selector('#book')
    text = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element( (By.ID, 'price'), '$100' ))
    btn.click()
    
    x = int(browser.find_element_by_css_selector('#input_value').text)

    answer_value = calc(x)
    answer_field = browser.find_element_by_id('answer')
    answer_field.send_keys(answer_value)


    button = browser.find_element_by_css_selector("button.btn[type='submit']")
    button.click()
    
    time.sleep(1)


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(25)
    # закрываем браузер после всех манипуляций
    browser.quit()



