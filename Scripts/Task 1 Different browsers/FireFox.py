from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = False

driver = webdriver.Firefox(
    executable_path='C:\\ProgramData\\Selenium\\geckodriver.exe',
    firefox_binary='C:\\Users\\stanislav.urasov\\Downloads\\FirefoxPortableESR\\Firefox.exe'  # 45 esr
#    firefox_binary='C:\\Program Files\\Mozilla Firefox\\firefox.exe' #new FF
)
driver.get("https://google.com")
assert "Google" in driver.title
driver.find_element_by_name("q").click()
driver.find_element_by_name("q").send_keys("Apriorit")
driver.find_element_by_name("q").submit()

assert "Apriorit - Пошук Google" in driver.title
driver.close()