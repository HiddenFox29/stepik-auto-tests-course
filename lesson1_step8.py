
import time

from selenium import webdriver


# используем менеджер контекста для гарантированного закрытия сессии
with webdriver.Chrome() as wd:
    # ссылка которая проходит тест
    # link = " http://suninjuly.github.io/registration1.html"

    # ссылка которая не проходит тест
    link = "http://suninjuly.github.io/registration1.html"
    wd.get(link)

    # Ваш код, который заполняет обязательные поля
    # для трех контейнеров прямых потомков контенера div[@class="first_block"]
    for elem in range(1, 4):
        # в цикле с помощью форматирования стоки подставляем в xpath номер дочернего элемента
        el = wd.find_element_by_xpath(f'/html/body/div[1]/form/div[@class="first_block"]/div[{elem}]/input')
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
    time.sleep(5)
    # благодаря менеджеру контеста браузер после всех манипуляций закроется сам