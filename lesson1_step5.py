
import time

from selenium import webdriver

with webdriver.Chrome() as wd:
    wd.get("http://suninjuly.github.io/huge_form.html")
    elements = wd.find_elements_by_tag_name('input')
    for element in elements:
        element.send_keys('answer')

    button = wd.find_element_by_css_selector('button.btn')
    button.click()
    time.sleep(20)
