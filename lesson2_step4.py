import math
import time

from selenium import webdriver

with webdriver.Chrome() as wd:
    wd.get('http://SunInJuly.github.io/execute_script.html')

    x = wd.find_element_by_id('input_value').text

    res = str(math.log(abs(12*math.sin(int(x)))))

    button = wd.find_element_by_tag_name('button')

    wd.execute_script("return arguments[0].scrollIntoView(true);", button)
    wd.find_element_by_id('answer').send_keys(res)

    wd.find_element_by_id('robotCheckbox').click()
    wd.execute_script("return arguments[0].scrollIntoView(true);", wd.find_element_by_id('robotsRule'))
    wd.find_element_by_id('robotsRule').click()
    button.click()

    time.sleep(10)