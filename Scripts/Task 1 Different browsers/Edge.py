from selenium import webdriver

from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://google.com")
assert "Google" in driver.title
driver.find_element_by_name("q").click()
driver.find_element_by_name("q").send_keys("Apriorit").submit()
print(driver.title)
assert "Apriorit - Пошук Google" in driver.title



driver.close()