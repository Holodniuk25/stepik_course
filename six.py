from os import link
import os
import time
from selenium import webdriver 

browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/file_input.html'



  
try:
    browser.get(link)
   
    inputs = browser.find_elements_by_css_selector('input[type="text"]')
    for inp in inputs:
        inp.send_keys('text')

    dir = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(dir, 'text.txt')
    browser.find_element_by_id('file').send_keys(full_path)


    # select = Select(browser.find_element_by_id('dropdown'))
    # select.select_by_visible_text( str( int(num1) + int(num2) ))


    button = browser.find_element_by_css_selector("button.btn[type='submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()