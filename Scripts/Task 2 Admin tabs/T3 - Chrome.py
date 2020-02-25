from time import sleep

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("http://localhost/litecart/public_html/")
assert "Training project" in driver.title


try:
    wait = WebDriverWait(driver, 300)
    element = wait.until(EC.presence_of_element_located((By.ID, "box-campaign-products")))
except selenium.common.exceptions.NoSuchElementException:
    print("Can't load site")
    exit(-1)

try:
    ducks = driver.find_elements_by_class_name("product-column")
except selenium.common.exceptions.NoSuchElementException:
    print("There are no ducks...")
    exit(-1)

i = 0
for duck in ducks:
    if duck.find_element_by_xpath("a / div[1] / div[1]") and not duck.find_elements_by_xpath("a / div[1] / div[2]"):
        print("It's alright, duck {0} have only 1 label: {1}"
              .format(duck.find_element_by_xpath("a/div[2]/div[1]").text, duck.find_element_by_xpath("a / div[1] / div").text))
    elif not duck.find_element_by_xpath("a / div[1] / div"):
        print("There is no label on the duck {0}"
              .format(duck.find_element_by_xpath("a/div[2]/div[1]").text))
    elif duck.find_element_by_xpath("a / div[1] / div") and duck.find_elements_by_xpath("a / div[1] / div[2]"):
        print("There are more than 1 label on the duck - {0}"
              .format(duck.find_element_by_xpath("a/div[2]/div[1]").text))

sleep(10)
driver.close()