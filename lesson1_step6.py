
import time

from selenium import webdriver

with webdriver.Chrome() as wd:
    wd.get('http://suninjuly.github.io/find_xpath_form')
    input_f_name = wd.find_element_by_tag_name('input')
    input_f_name.send_keys('Ivan')

    input_l_name = wd.find_element_by_name('last_name')
    input_l_name.send_keys('Petrov')

    input_c_name = wd.find_element_by_class_name('city')
    input_c_name.send_keys('Smolensk')

    input_ctr_name = wd.find_element_by_id('country')
    input_ctr_name.send_keys('Russia')

    button = wd.find_element_by_xpath('/html/body/div[1]/form/div[6]/button[3]')
    button.click()
    time.sleep(30)
