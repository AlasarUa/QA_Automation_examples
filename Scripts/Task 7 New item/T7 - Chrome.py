# Сделайте сценарий для добавления нового товара (продукта) в учебном приложении litecart (в админке).
# Для добавления товара нужно открыть меню Catalog, в правом верхнем углу нажать кнопку "Add New Product", заполнить поля с информацией о товаре и сохранить.
# Достаточно заполнить только информацию на вкладках General, Information и Prices. Скидки (Campains) на вкладке Prices можно не добавлять.
# После сохранения товара нужно убедиться, что он появился в каталоге (в админке). Клиентскую часть магазина можно не проверять.
# Можно оформить сценарий либо как тест, либо как отдельный исполняемый файл.

from random import random
from time import sleep
import names
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("http://localhost/litecart/public_html/admin/login.php")
    wait = WebDriverWait(driver, 300)
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"box-login\"]/form/div[2]/button")))
    assert "Training project" in driver.title
except selenium.common.exceptions.NoSuchElementException:
    print("Can't load site")
    exit(-1)

try:
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("username").submit()
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("password").submit()
    wait = WebDriverWait(driver, 300)
    element = wait.until(EC.presence_of_element_located((By.ID, "box-apps-menu")))
except selenium.common.exceptions.NoSuchElementException:
    print("There is problem with login")
    exit(-1)

sleep(2)
driver.find_element_by_css_selector("#box-apps-menu > li:nth-child(2)").click()

try:
    wait = WebDriverWait(driver, 300)
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content > div > div.panel-action > ul > li:nth-child(2) > a")))
    driver.find_element_by_css_selector("#content > div > div.panel-action > ul > li:nth-child(2) > a").click()
except selenium.common.exceptions.NoSuchElementException:
    print("problem")
    exit(-1)

name = names.get_last_name() + " duck"
sleep(1)
driver.find_element_by_css_selector("#tab-general > div > div:nth-child(2) > div:nth-child(1) > div > input").send_keys(name)
driver.find_element_by_css_selector("#tab-general > div > div:nth-child(2) > div:nth-child(2) > input").send_keys(names.get_last_name())
sleep(1)
driver.find_element_by_xpath("//*[@id=\"categories\"]/div[2]/label").click()
driver.find_element_by_xpath("//*[@id=\"tab-general\"]/div/div[2]/div[4]/div/select").click()
driver.find_element_by_xpath("//*[@id=\"tab-general\"]/div/div[2]/div[4]/div/select/option[2]").click()
# driver.find_element_by_xpath("//*[@id=\"tab-general\"]/div/div[2]/div[3]/div[1]/input").send_keys(1)

driver.find_element_by_xpath("//*[@id=\"content\"]/div/ul/li[2]/a").click()
driver.find_element_by_xpath("//*[@id=\"en\"]/div[1]/div/input").send_keys("This is an awesome " + name)

driver.find_element_by_xpath("//*[@id=\"content\"]/div/ul/li[4]/a").click()
driver.find_element_by_xpath("//*[@id=\"prices\"]/div/div[1]/div/input").send_keys(15)
driver.find_element_by_xpath("//*[@id=\"prices\"]/div/div[1]/div/span/div/select").click()
driver.find_element_by_xpath("//*[@id=\"prices\"]/div/div[1]/div/span/div/select/option[2]").click()


driver.find_element_by_xpath("//*[@id=\"content\"]/div/ul/li[6]/a").click()
driver.find_element_by_xpath("//*[@id=\"table-stock\"]/tbody/tr/td[5]/input").send_keys(10)

driver.find_element_by_xpath("//*[@id=\"content\"]/div/div[2]/form/div[2]/button[1]").click()

try:
    wait = WebDriverWait(driver, 300)
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"content\"]/div[2]/div[3]/form/table/tbody/tr[1]/td[3]")))
except selenium.common.exceptions.NoSuchElementException:
    print("problem")
    exit(-1)

root_items = driver.find_elements_by_css_selector("#content > div.panel.panel-app > div.panel-body > form > table > tbody > tr.semi-transparent > td > a")
root_items_names = []

for item in root_items:
    try:
        root_items_names.append(item.get_property("text"))
    except AttributeError:
        print("try again")
for item in root_items_names:
    if name == item:
        print("Item \"" + name + "\" was successfully created")
        exit(0)
    else:
        print(item + "not equal " + name)


sleep(10)
driver.close()
