
import time
import math

from selenium import webdriver

with webdriver.Chrome() as wd:
    wd.get('http://suninjuly.github.io/redirect_accept.html')
    wd.find_element_by_css_selector('button.trollface').click()
    
    # команда для работы с окнами и вкладками switch_to
    print(wd.window_handles)
    # команда для работы с окнами window -> принемает имя окна для переключения
    wd.switch_to.window(wd.window_handles[1])
    x = wd.find_element_by_id('input_value').text
    wd.find_element_by_id('answer').send_keys(
        str(math.log(abs(12*math.sin(int(x))))))
    wd.find_element_by_css_selector('button.btn').click()
    time.sleep(20)



