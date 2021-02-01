
import os
import time

from selenium import webdriver


current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = None
try:
    if not os.path.exists(current_dir + '/file.txt'):
        with open(current_dir + '/file.txt', 'w'): pass
        file_path = os.path.join(current_dir, 'file.txt')
    else:
        file_path = os.path.join(current_dir, 'file.txt')
except OSError as er:
    print(er)

with webdriver.Chrome() as wd:
    wd.get('http://suninjuly.github.io/file_input.html')
    wd.find_element_by_css_selector('input[name=firstname]').send_keys('ivan')
    wd.find_element_by_css_selector('input[name=lastname]').send_keys('ivanov')
    wd.find_element_by_css_selector('input[name=email]').send_keys('ivan@mail.ru')

    wd.find_element_by_css_selector('input[type=file]').send_keys(file_path)
    wd.find_element_by_css_selector('button.btn').click()
    time.sleep(20)



