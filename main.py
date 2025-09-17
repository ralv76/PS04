from selenium import webdriver
import time
import random
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

print("=== !!! ВАЖНО !!! ===\nЕсть разные типы страницы, под них не адаптировал весь код. \nВариант корректной отработки всех пунктов - по поисковой фразе ПАНАМА.")

browser = webdriver.Firefox()

word = input("Введите ключевой запрос:")
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
#assert "Википедия" in browser.title
time.sleep(7)
search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys(word)
search_box.send_keys(Keys.RETURN)
time.sleep(5)
a = browser.find_element(By.LINK_TEXT, word)
a.click()
time.sleep(5)

print(f"Первоначальная страница по фразе {word} найдена, входим в меню")
      
while True:
    command = input("\nНажмите:\n0 - для выхода;\n1 - для чтения параграфов текущей статьи;\n2 - перейти на любую случайную статью из указанных на странице;\n3 - ввести новое слово для поиска")
    if command == "0":
        print("спасибо - до свидания")
        browser.quit()
        break
    #if command == "2":
    #    hatnotes = []
    #    for element in browser.find_elements(By.TAG_NAME, "div"):
    #        cl = element.get_attribute("class")
    #        if cl == "hatnote navigation-not-searchable ts-main":
    #            hatnotes.append(element)
    #    #print(hatnotes)
    #    hatnote = random.choice(hatnotes)
    #    link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
    #    browser.get(link)
    if command == "2":
        hatnotes = []
        # Ищем все div-эlements с классом, который содержит слово 'hatnote'
        for element in browser.find_elements(By.CSS_SELECTOR, "div.hatnote"):
            hatnotes.append(element)
        if hatnotes: # Проверяем, что список не пустой
            hatnote = random.choice(hatnotes)
            link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
            browser.get(link)
        else:
            print("На этой странице не найдено подходящих ссылок для перехода.")
    if command == "1":
        paragraphs = browser.find_elements(By.TAG_NAME, "p")
        for paragraph in paragraphs:
            if paragraph.text.strip():  # Проверяем, что параграф не пустой
                print(paragraph.text)
                user_input = input("...Нажмите Enter для продолжения или 'q' для выхода...")
                if user_input.lower() == 'q':
                    break
        word = input("Введите ключевой запрос:")
        browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
        #assert "Википедия" in browser.title
        time.sleep(7)
        search_box = browser.find_element(By.ID, "searchInput")
        search_box.send_keys(word)
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)
        a = browser.find_element(By.LINK_TEXT, word)
        a.click()
        time.sleep(5)
    if command not in {"0", "1", "2", "3"}:
        print("Непонятно.")



#paragraphs = browser.find_elements(By.TAG_NAME, "p")
#for paragraph in paragraphs:
#    print(paragraph.text)
#    input()


#browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")

