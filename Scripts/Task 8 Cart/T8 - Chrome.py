# Сделайте сценарий для добавления товаров в корзину и удаления товаров из корзины.
# Сценарий должен состоять из следующих частей:
# 1) открыть страницу какого-нибудь товара
# 2) добавить его в корзину
# 3) подождать, пока счётчик товаров в корзине обновится
# 4) вернуться на главную страницу, повторить предыдущие шаги ещё два раза, чтобы в общей сложности в корзине было 3 единицы товара
# 5) открыть корзину (в правом верхнем углу кликнуть по ссылке Checkout)
# 6) удалить все товары из корзины один за другим, после каждого удаления подождать, пока внизу обновится таблица
from random import random, randint
from time import sleep
import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("http://localhost/litecart/public_html/")
    wait = WebDriverWait(driver, 3)
    element = wait.until(EC.visibility_of_all_elements_located((By.ID, "box-campaign-products")))
    assert "Training project" in driver.title
except selenium.common.exceptions.NoSuchElementException:
    print("Can't load site")
    exit(-1)

quantity = 0

while quantity < 3:
    try:
        products = driver.find_elements_by_class_name("product-column")
    except selenium.common.exceptions.NoSuchElementException:
        print("Can't find products")
        exit(-1)

    try:
        products.pop(randint(1, len(products) - 1)).click()
        element = wait.until(EC.visibility_of_all_elements_located((By.NAME, "add_cart_product")))
    except selenium.common.exceptions.NoSuchElementException:
        print("Can't load product page")
        exit(-1)

    try:
        driver.find_element_by_name("add_cart_product").click()
        element = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id=\"cart\"]/a/div")))
    except selenium.common.exceptions.NoSuchElementException:
        print("¯\_(ツ)_/¯")
        exit(-1)
    finally:
        sleep(1)

    if quantity < int(driver.find_element_by_xpath("//*[@id=\"cart\"]/a/div").get_property("textContent")):
        quantity = int(driver.find_element_by_xpath("//*[@id=\"cart\"]/a/div").get_property("textContent"))
        print("Product added to the cart. There is {0} product(s) in the cart".format(quantity))
    else:
        print("There is something strange")
    driver.find_element_by_xpath("//*[@id=\"header\"]/a").click()

# open cart
driver.find_element_by_xpath("//*[@id=\"cart\"]/a").click()

#to do
# 6) удалить все товары из корзины один за другим, после каждого удаления подождать, пока внизу обновится таблица
