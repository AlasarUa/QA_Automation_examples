from selenium import webdriver


driver = webdriver.Ie()
driver.get("https://google.com")

assert "Google" in driver.title
driver.find_element_by_name("q").click()
driver.find_element_by_name("q").send_keys("Apriorit")
driver.find_element_by_name("q").submit()
assert "Google" in driver.title
driver.close()