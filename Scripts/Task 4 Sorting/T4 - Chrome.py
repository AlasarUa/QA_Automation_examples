from time import sleep

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

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

driver.get("http://localhost/litecart/public_html/admin/?app=countries&doc=countries")

try:
    wait = WebDriverWait(driver, 300)
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content > div > div.panel-body > form")))
except selenium.common.exceptions.NoSuchElementException:
    print("There are no countries...")
    exit(-1)

countries = driver.find_elements_by_css_selector("#content > div > div.panel-body > form > table > tbody > tr")
countries_name = []
countries_with_zones = {}
countries_with_zones_links = []
zones = []
zones_name = []

for country in countries:
    countries_name.append(country.find_element_by_xpath("td[5]/a").text)

    if int(country.find_element_by_xpath("td[6]").text) > 0:
        name = country.find_element_by_xpath("td[5]/a").text
        href = country.find_element_by_xpath("td[5]/a").get_property("href")
        countries_with_zones.update({name: href})

countries_name_sorted = countries_name.copy()
countries_name_sorted.sort()

if countries_name_sorted != countries_name:
    print("Countries in the list isn't sorted")
    print(countries_name)
    print(countries_name_sorted)

for country in countries_with_zones:
    driver.get(countries_with_zones.get(country))
    try:
        wait = WebDriverWait(driver, 300)
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"content\"]/div/div[2]/form/table")))
    except selenium.common.exceptions.NoSuchElementException:
        print("There are no zones in the {0}".format(country))

    sleep(2)
    zones = driver.find_elements_by_class_name("form-control")
    zones_name.clear()

    for zone in zones:
        if "zones" in zone.get_property("name") and "name" in zone.get_property("name"):
            zones_name.append(zone.get_property("value"))

    zones_name_sorted = zones_name.copy()
    zones_name_sorted.sort()

    if zones_name != zones_name_sorted:
        print("Zones in the {0} aren't sorted".format(country))
    else:
        print("{0} has zones and they are sorted".format(country))

sleep(10)
driver.close()