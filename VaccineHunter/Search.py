
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = 'https://appointments.vaccinehunters.ca/search/<<postal code>>'
driver.get(URL)

print(driver.title)

elems = driver.find_elements_by_tag_name("a")
for elem in elems:
    print(elem.get_attribute("href"))
    href = elem.get_attribute("href")
    if not href.startswith('https://appointments.vaccinehunters.ca/')  :
        openscript = "window.open('" + href + "','_blank');"
        driver.execute_script(openscript)

driver.stop_client()

#search_bar = driver.find_element_by_name("q")

# search_bar.clear()
# search_bar.send_keys("<<full name>>")
# search_bar.send_keys(Keys.RETURN)




