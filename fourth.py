import math
from selenium import webdriver
import time 


link = "http://suninjuly.github.io/math.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    
    browser = webdriver.Chrome()
    browser.get(link)
    x = int(browser.find_element_by_css_selector('#input_value').text)

    answer_value = calc(x)
    answer_field = browser.find_element_by_id('answer')
    answer_field.send_keys(answer_value)

    browser.find_element_by_id('robotCheckbox').click()

    browser.find_element_by_id('robotsRule').click()

    button = browser.find_element_by_css_selector("button.btn[type='submit']")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()



