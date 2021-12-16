import math
from os import link
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


browser = webdriver.Chrome()
link = 'http://SunInJuly.github.io/execute_script.html'


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

  
try:
    browser.get(link)
    x = int(browser.find_element_by_css_selector('#input_value').text)
    print(x)
    answer_value = calc(x)
    print(answer_value)
    answer_field = browser.find_element_by_id('answer')
    answer_field.send_keys(answer_value)


    # select = Select(browser.find_element_by_id('dropdown'))
    # select.select_by_visible_text( str( int(num1) + int(num2) ))

    checkbox = browser.find_element_by_id('robotCheckbox')
    browser.execute_script(' arguments[0].scrollIntoView(true)', checkbox)
    checkbox.click()
    browser.find_element_by_id('robotsRule').click()

    button = browser.find_element_by_css_selector("button.btn[type='submit']")
    button.click()
   
    

    button = browser.find_element_by_css_selector("button.btn[type='submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()