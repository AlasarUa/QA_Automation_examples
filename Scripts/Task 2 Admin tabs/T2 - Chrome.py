from time import sleep

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
i = 1

while i < len(categories) + 1:
    try:
        driver.find_element_by_css_selector("ul#box-apps-menu li.app:nth-child({0}) a".format(str(i))).click()
    finally:
        sleep(2)

    subcategories = driver.find_elements_by_css_selector("ul#box-apps-menu li.app:nth-child({0}) li".format(str(i)))
    print(len(subcategories))
    category_name = driver.find_element_by_css_selector("#box-apps-menu li.app.selected a span.name").text
    j = 2

    print(category_name.text + " => " + driver.find_element_by_class_name("panel-heading").text)

    while len(subcategories) >= j:
        driver.find_element_by_css_selector("ul#box-apps-menu li.app.selected li:nth-child({0})".format(str(j))).click()
        sleep(2)
        print(category_name + " => " + driver.find_element_by_class_name("panel-heading").text)
        j += 1
    i += 1

driver.implicitly_wait(10)

# driver.find_elements_by_css_selector("ul#box-apps-menu ul.docs li.doc").click()

# driver.close()
