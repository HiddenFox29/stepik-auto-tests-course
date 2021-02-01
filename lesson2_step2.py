
import math
import time

from selenium import webdriver

with webdriver.Chrome() as wd:
    wd.get('http://suninjuly.github.io/get_attribute.html')

    get_treasure = wd.find_element_by_id('treasure')
    x = get_treasure.get_attribute("valuex")
    res = str(math.log(abs(12*math.sin(int(x)))))
    answer = wd.find_element_by_id('answer')
    answer.send_keys(res)

    checkbox = wd.find_element_by_id('robotCheckbox')
    checkbox.click()

    radio = wd.find_element_by_id('robotsRule')
    radio.click()

    btn = wd.find_element_by_css_selector('button.btn')
    btn.click()

    time.sleep(10)

