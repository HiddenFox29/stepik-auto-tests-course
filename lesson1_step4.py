
import time
import math

from selenium import webdriver

from managerContextWebdriver import Webdriver

link = ' http://suninjuly.github.io/find_link_text'

with Webdriver(webdriver.Chrome()) as wd:
    wd.get(link)

    link_math = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link_click = wd.find_element_by_link_text(link_math)
    link_click.click()

    input_f_name = wd.find_element_by_tag_name('input')
    input_f_name.send_keys('Ivan')

    input_l_name = wd.find_element_by_name('last_name')
    input_l_name.send_keys('Petrov')

    input_c_name = wd.find_element_by_class_name('city')
    input_c_name.send_keys('Smolensk')

    input_ctr_name = wd.find_element_by_id('country')
    input_ctr_name.send_keys('Russia')

    button = wd.find_element_by_css_selector('button.btn')
    button.click()
    time.sleep(30)