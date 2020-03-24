# Сделайте сценарий, который проверяет, что при клике на товар открывается правильная страница товара в учебном приложении litecart.
# 1) Открыть главную страницу
# 2) Кликнуть по первому товару в категории Campaigns
# 3) Проверить, что открывается страница правильного товара
# Более точно, проверить, что
# а) совпадает текст названия товара
# б) совпадает цена (обе цены)
# Кроме того, проверить стили цены на главной странице и на странице товара -- первая цена серая, зачёркнутая, маленькая, вторая цена красная жирная, крупная.

from time import sleep
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://localhost/litecart/public_html/")
    wait = WebDriverWait(driver, 300)
    element = wait.until(EC.presence_of_element_located((By.ID, "box-campaign-products")))
    assert "Training project" in driver.title
except selenium.common.exceptions.NoSuchElementException:
    print("Can't load site")
    exit(-1)

product_main = dict(object=driver.find_element_by_xpath("//*[@id=\"box-campaign-products\"]/div/article[1]"),
                    name=driver.find_element_by_xpath(
                        "//*[@id=\"box-campaign-products\"]/div/article[1]/a/div[2]/div[1]").get_property(
                        "textContent"),
                    regular_price=driver.find_element_by_css_selector(
                        "#box-campaign-products > div > article:nth-child(1) > a > div.info > div.price-wrapper > del")
                    .get_property("textContent"),
                    regular_price_style=driver.find_element_by_css_selector(
                        "#box-campaign-products > div > article:nth-child(1) > a > div.info > div.price-wrapper > del")
                    .value_of_css_property("font"),
                    regular_price_color=driver.find_element_by_css_selector(
                        "#box-campaign-products > div > article:nth-child(1) > a > div.info > div.price-wrapper > del")
                    .value_of_css_property("color"),
                    regular_price_decoration=driver.find_element_by_css_selector(
                        "#box-campaign-products > div > article:nth-child(1) > a > div.info > div.price-wrapper > del")
                    .value_of_css_property("text-decoration"),
                    campaign_price=driver.find_element_by_css_selector(
                        "#box-campaign-products > div > article:nth-child(1) > a > div.info > div.price-wrapper > strong")
                    .get_property("textContent"),
                    campaign_price_style=driver.find_element_by_css_selector(
                        "#box-campaign-products > div > article:nth-child(1) > a > div.info > div.price-wrapper > strong")
                    .value_of_css_property("font"),
                    campaign_price_color=driver.find_element_by_css_selector(
                        "#box-campaign-products > div > article:nth-child(1) > a > div.info > div.price-wrapper > strong")
                    .value_of_css_property("color"),
                    campaign_price_decoration=driver.find_element_by_css_selector(
                        "#box-campaign-products > div > article:nth-child(1) > a > div.info > div.price-wrapper > strong")
                    .value_of_css_property("font-weight"))

print(product_main.get("name"))

driver.find_element_by_xpath("//*[@id=\"box-campaign-products\"]/div/article[1]/a/div[2]/div[1]").click()

product_page = dict(name=driver.find_element_by_css_selector("#box-product > div.row > div.col-sm-8.col-md-6 > h1").get_property("textContent"),
                    regular_price=driver.find_element_by_css_selector("#box-product > div.row > div.col-sm-8.col-md-6 > div.buy_now > form > div.price-wrapper > del").get_property("textContent"),
                    regular_price_style=driver.find_element_by_css_selector("#box-product > div.row > div.col-sm-8.col-md-6 > div.buy_now > form > div.price-wrapper > del").value_of_css_property("font"),
                    regular_price_color=driver.find_element_by_css_selector("#box-product > div.row > div.col-sm-8.col-md-6 > div.buy_now > form > div.price-wrapper > del").value_of_css_property("color"),
                    regular_price_decoration=driver.find_element_by_css_selector("#box-product > div.row > div.col-sm-8.col-md-6 > div.buy_now > form > div.price-wrapper > del").value_of_css_property("text-decoration"),
                    campaign_price=driver.find_element_by_css_selector("#box-product > div.row > div.col-sm-8.col-md-6 > div.buy_now > form > div.price-wrapper > strong").get_property("textContent"),
                    campaign_price_style=driver.find_element_by_css_selector("#box-product > div.row > div.col-sm-8.col-md-6 > div.buy_now > form > div.price-wrapper > strong").value_of_css_property("font"),
                    campaign_price_color=driver.find_element_by_css_selector("#box-product > div.row > div.col-sm-8.col-md-6 > div.buy_now > form > div.price-wrapper > strong").value_of_css_property("color"),
                    campaign_price_decoration=driver.find_element_by_css_selector("#box-product > div.row > div.col-sm-8.col-md-6 > div.buy_now > form > div.price-wrapper > strong").value_of_css_property("font-weight"))

if product_main.get("name") == product_page.get("name"):
    print("The Name is the same")
else:
    print("The Name is wrong")

if product_main.get("regular_price") == product_page.get("regular_price"):
    print("The regular price is the same")
else:
    print("The regular price is wrong")

if product_main.get("campaign_price") == product_page.get("campaign_price"):
    print("The campaign price is the same")
else:
    print("The campaign price is wrong")

#  product_main.get("regular_price_style") == product_page.get("regular_price_style") and \

if product_main.get("regular_price_color") == product_page.get("regular_price_color") and \
   product_main.get("regular_price_decoration") == product_page.get("regular_price_decoration"):
    print("The regular price style is the same")
else:
    print("The regular price style is wrong")
    print(product_main.get("regular_price_style") + ", " + product_main.get("regular_price_color") + ", " + product_main.get("regular_price_decoration"))
    print(product_page.get("regular_price_style") + ", " + product_page.get("regular_price_color") + ", " + product_page.get("regular_price_decoration"))

#   product_main.get("campaign_price_style") == product_page.get("campaign_price_style") and \

if \
   product_main.get("campaign_price_color") == product_page.get("campaign_price_color") and \
   product_main.get("campaign_price_decoration") == product_page.get("campaign_price_decoration"):
    print("The campaign price style is the same")
else:
    print("The campaign price style is wrong")
    print(product_main.get("campaign_price_style") + ", " + product_main.get("campaign_price_color") + ", " + product_main.get("campaign_price_decoration"))
    print(product_page.get("campaign_price_style") + ", " + product_page.get("campaign_price_color") + ", " + product_page.get("campaign_price_decoration"))

sleep(10)
driver.close()
