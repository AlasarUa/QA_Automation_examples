# Сделайте сценарий, который выполняет следующие действия в учебном приложении litecart.
# 1) входит в панель администратора http://localhost/litecart/admin
# 2) прокликивает последовательно все пункты меню слева, включая вложенные пункты
# 3) для каждой страницы проверяет наличие заголовка

from time import sleep
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://localhost/litecart/public_html/admin/login.php")
assert "Training project" in driver.title

driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("username").submit()
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("password").submit()

assert "admin" in driver.current_url

try:
    wait = WebDriverWait(driver, 300)
    element = wait.until(EC.presence_of_element_located((By.ID, "box-apps-menu")))
finally:
    print(driver.current_url + " loaded")

categories = driver.find_elements_by_css_selector("ul#box-apps-menu li.app")
print("There are " + str(len(categories)) + " categories in this menu")
i = 1
sleep(2)

while i < len(categories) + 1:
    driver.find_element_by_css_selector("ul#box-apps-menu li.app:nth-child({0}) a".format(str(i))).click()
    wait = WebDriverWait(driver, 300)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "panel-heading")))

    sleep(2)

    subcategories = driver.find_elements_by_css_selector("ul#box-apps-menu li.app:nth-child({0}) li".format(str(i)))
    print(len(subcategories))
    category_name = driver.find_element_by_css_selector("#box-apps-menu li.app.selected a span.name").text
    j = 2

    try:
        print(category_name + " => " + driver.find_element_by_class_name("panel-heading").text)
    except selenium.common.exceptions.NoSuchElementException:
        print("There is no header")

    while len(subcategories) >= j:
        driver.find_element_by_css_selector("ul#box-apps-menu li.app.selected li:nth-child({0})".format(str(j))).click()
        sleep(2)
        try:
            print(category_name + " => " + driver.find_element_by_class_name("panel-heading").text)
        except selenium.common.exceptions.NoSuchElementException:
            print("There is no header")
        j += 1
    i += 1

sleep(10)
driver.close()
