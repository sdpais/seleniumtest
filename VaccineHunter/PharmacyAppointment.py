
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome(ChromeDriverManager().install())

URL = 'https://www.pharmacyappointments.ca/'
driver.get(URL)

print(driver.title)
passed=False
WebDriverWait(driver, 3)
#page 1 - Select Language
elems = driver.find_elements_by_tag_name("select")
for elem in elems:
    print(elem.get_attribute("aria-labelledby"))
    attribute = elem.get_attribute("aria-labelledby")
    if  attribute.startswith('language-select')  :
        select = Select(elem)
        select.select_by_value('en_CA')
        passed = True
        break

if passed :
    passed= False
    elems = driver.find_elements_by_tag_name("button")
    for elem in elems:
        buttondata = elem.get_attribute("data-testid")
        if buttondata == 'landing-page-continue' :
            elem.click()
            passed=True
            break

WebDriverWait(driver, 3)
#page 2 - Select Province
if passed :
    passed= False
    elems = driver.find_elements_by_tag_name("select")
    for elem in elems:
        print(elem.get_attribute("id"))
        attribute = elem.get_attribute("id")
        if  attribute.startswith('q-screening-province')  :
            select = Select(elem)
            select.select_by_value('Ontario')
            passed = True
            break

if passed :
    passed= False
    elems = driver.find_elements_by_tag_name("input")
    for elem in elems:
        print(elem.get_attribute("id"))
        attribute = elem.get_attribute("id")
        if  attribute.startswith('q-screening-ontario-province-Yes')  :
            elem.click()
            passed = True
            break

if passed :
    passed= False
    elems = driver.find_elements_by_tag_name("input")
    for elem in elems:
        print(elem.get_attribute("id"))
        attribute = elem.get_attribute("id")
        if  attribute.startswith('q-screening-ontario-first-or-second-dose-Second Dose')  :
            elem.click()
            passed = True
            break
if passed :
    passed= False
    elems = driver.find_elements_by_tag_name("input")
    for elem in elems:
        print(elem.get_attribute("id"))
        attribute = elem.get_attribute("id")
        if  attribute.startswith('q-screening-ontario-product-Pfizer')  :
            elem.click()
            passed = True
            break
if passed :
    passed= False
    elems = driver.find_elements_by_tag_name("input")
    for elem in elems:
        print(elem.get_attribute("id"))
        attribute = elem.get_attribute("id")
        if  attribute.startswith('q-screening-ontario-pfizer-second-dose-Yes')  :
            elem.click()
            elem.send_keys("<<enter postal code>>")
            passed = True
            break

if passed :
    passed= False
    elems = driver.find_elements_by_tag_name("button")
    for elem in elems:
        buttondata = elem.get_attribute("data-testid")
        if buttondata == 'continue-button' :
            elem.click()
            passed=True
            break


WebDriverWait(driver, 3)
#page 3 - Select Location

if passed :
    passed= False
    elems = driver.find_elements_by_tag_name("input")
    for elem in elems:
        print(elem.get_attribute("id"))
        attribute = elem.get_attribute("id")
        if  attribute.startswith('location-search-address')  :
            elem.click()
            elem.send_keys("<<enter postal code>>")
            passed = True
            break

if passed :
    passed= False
    elems = driver.find_elements_by_tag_name("button")
    for elem in elems:
        buttondata = elem.get_attribute("data-testid")
        if buttondata == 'location-search-page-continue' :
            elem.click()
            passed=True
            break



driver.stop_client()

#search_bar = driver.find_element_by_name("q")

# search_bar.clear()
# search_bar.send_keys("<<full name>>")
# search_bar.send_keys(Keys.RETURN)

