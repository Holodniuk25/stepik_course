from selenium import webdriver
import time 


link = "http://suninjuly.github.io/huge_form.html"
from selenium.webdriver.common.by import By
try:
    
    browser = webdriver.Chrome()
    browser.get(link)
    inputs = browser.find_elements_by_css_selector('input[type="text"]')
    print(inputs)
    for input in inputs:
        input.send_keys('Answer')
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()