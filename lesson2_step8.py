
import time
import math

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



with webdriver.Chrome() as wd:
    wd.get('http://suninjuly.github.io/explicit_wait2.html')
    price = WebDriverWait(wd, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
        )
    wd.find_element_by_id('book').click()

    # команда для работы с окнами и вкладками switch_to
    print(wd.window_handles)
    # команда для работы с окнами window -> принемает имя окна для переключения
    x = wd.find_element_by_id('input_value').text
    wd.find_element_by_id('answer').send_keys(
        str(math.log(abs(12*math.sin(int(x))))))
    wd.find_element_by_id('solve').click()
    time.sleep(20)



