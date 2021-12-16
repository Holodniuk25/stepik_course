import math
from selenium import webdriver
import time 


link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    
    browser = webdriver.Chrome()
    browser.get(link)
    

    browser.find_element_by_css_selector('button').click()
    new_window = browser.window_handles[1]
    alert = browser.switch_to.window(new_window)
    time.sleep(1)


    x = int(browser.find_element_by_css_selector('#input_value').text)

    answer_value = calc(x)
    answer_field = browser.find_element_by_id('answer')
    answer_field.send_keys(answer_value)


    button = browser.find_element_by_css_selector("button.btn[type='submit']")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()



