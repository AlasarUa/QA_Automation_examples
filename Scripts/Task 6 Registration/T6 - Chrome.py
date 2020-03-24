# Сделайте сценарий для регистрации нового пользователя в учебном приложении litecart (не в админке, а в клиентской части магазина).
# Сценарий должен состоять из следующих частей:
# 1) регистрация новой учётной записи с достаточно уникальным адресом электронной почты (чтобы не конфликтовало с ранее созданными пользователями),
# 2) выход (logout), потому что после успешной регистрации автоматически происходит вход,
# 3) повторный вход в только что созданную учётную запись,
# 4) и ещё раз выход.

from time import sleep
import selenium
import names
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("http://localhost/litecart/public_html/")
    wait = WebDriverWait(driver, 300)
    element = wait.until(EC.presence_of_element_located((By.ID, "box-campaign-products")))
    assert "Training project" in driver.title
except selenium.common.exceptions.NoSuchElementException:
    print("Can't load site")
    exit(-1)

driver.find_element_by_xpath("//*[@id=\"default-menu\"]/ul[2]/li[2]/a").click()
driver.find_element_by_xpath("//*[@id=\"default-menu\"]/ul[2]/li[2]/ul/li[2]/a").click()

# user creation
email = names.get_last_name() + "@" + names.get_first_name('male') + "." + names.get_first_name('female')
password = "Apriorit!1"

driver.find_element_by_xpath("//*[@id=\"box-create-account\"]/form/div[2]/div[1]/input").send_keys(names.get_first_name('male'))
driver.find_element_by_xpath("//*[@id=\"box-create-account\"]/form/div[2]/div[2]/input").send_keys(names.get_last_name())
driver.find_element_by_xpath("//*[@id=\"box-create-account\"]/form/div[5]/div[1]/div/select").click()
driver.find_element_by_css_selector("#box-create-account > form > div:nth-child(6) > div:nth-child(1) > div > select > option:nth-child(227)").click()
driver.find_element_by_xpath("//*[@id=\"box-create-account\"]/form/div[6]/div[1]/div/input").send_keys(email)
driver.find_element_by_xpath("//*[@id=\"box-create-account\"]/form/div[7]/div[1]/div/input").send_keys(password)
driver.find_element_by_xpath("//*[@id=\"box-create-account\"]/form/div[7]/div[2]/div/input").send_keys(password)
driver.find_element_by_css_selector("#box-create-account > form > div.checkbox > label > input[type=checkbox]").click()
driver.find_element_by_css_selector("#box-create-account > form > div.btn-group > button").click()

sleep(5)

try:
    wait = WebDriverWait(driver, 300)
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#notices > div")))
except selenium.common.exceptions.NoSuchElementException:
    print("There is some error with user creation")
    exit(-1)

print("User created: \"" + email + "\" \"" + password + "\"")

# logout
driver.find_element_by_css_selector("#default-menu > ul.nav.navbar-nav.navbar-right > li.account.dropdown > a").click()
driver.find_element_by_css_selector("#default-menu > ul.nav.navbar-nav.navbar-right > li.account.dropdown.open > ul > li:nth-child(3) > a").click()


sleep(5)

# login
driver.find_element_by_css_selector("#default-menu > ul.nav.navbar-nav.navbar-right > li.account.dropdown > a").click()
driver.find_element_by_css_selector("#default-menu > ul.nav.navbar-nav.navbar-right > li.account.dropdown.open > ul > li:nth-child(1) > form > div.form-group.required > div > input").send_keys(email)
driver.find_element_by_css_selector("#default-menu > ul.nav.navbar-nav.navbar-right > li.account.dropdown.open > ul > li:nth-child(1) > form > div:nth-child(4) > div > input").send_keys(password)
driver.find_element_by_css_selector("#default-menu > ul.nav.navbar-nav.navbar-right > li.account.dropdown.open > ul > li:nth-child(1) > form > div.btn-group.btn-block > button").click()

try:
    wait = WebDriverWait(driver, 300)
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#notices > div")))
except selenium.common.exceptions.NoSuchElementException:
    print("There is some trouble with login")
    exit(-1)
sleep(5)

# logout
driver.find_element_by_css_selector("#default-menu > ul.nav.navbar-nav.navbar-right > li.account.dropdown > a").click()
driver.find_element_by_css_selector("#default-menu > ul.nav.navbar-nav.navbar-right > li.account.dropdown.open > ul > li:nth-child(3) > a").click()


sleep(10)
driver.close()
