from selenium import webdriver
import time


with webdriver.Chrome() as wd:
    link = "http://suninjuly.github.io/registration2.html"
    wd.get(link)

    # Ваш код, который заполняет обязательные поля
    for elem in range(1, 4):
        el = wd.find_element_by_xpath(f'/html/body/div[1]/form/div[1]/div[{elem}]/input')
        el.send_keys('ok')

    # Отправляем заполненную форму
    button = wd.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = wd.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
