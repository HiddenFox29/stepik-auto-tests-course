
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

with webdriver.Chrome() as wd:
    wd.get(' http://suninjuly.github.io/selects1.html')
    num1 = wd.find_element_by_id('num1').text
    num2 = wd.find_element_by_id('num2').text
    result = str(int(num1) + int(num2))
    select = Select(wd.find_element_by_tag_name('select'))
    select.select_by_value(result)

    btn = wd.find_element_by_css_selector('button.btn').click()

    time.sleep(20)
