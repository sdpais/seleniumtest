def find_and_enter_data_in_text_box_by_id(driver, id, text):
    elem = driver.find_element_by_id(id)
    elem.click()
    elem.send_keys(text)
def find_and_click_element_by_id(driver, id):
    elem = driver.find_element_by_id(id)
    elem.click()
def find_and_select_item_by_value_by_id(driver, id, value):
    elem = driver.find_element_by_id(id)
    select = Select(elem)
    select.select_by_value(value)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome(ChromeDriverManager().install())

URL = 'https://covid-19.ontario.ca/book-vaccine/'
driver.get(URL)
print(driver.title)

WebDriverWait(driver, 3)
#page 1 - Check
find_and_click_element_by_id(driver, "dose_2")
find_and_click_element_by_id(driver, "vaccine_3")
find_and_enter_data_in_text_box_by_id(driver, "first_dose_day", "22")
find_and_select_item_by_value_by_id(driver, "first_dose_month", "4")
find_and_enter_data_in_text_box_by_id(driver, "postal_code_input", "M2R 2L9")
find_and_enter_data_in_text_box_by_id(driver, "birthyear_input", "2004")
find_and_click_element_by_id(driver, "health_card_green")
find_and_click_element_by_id(driver, "priority_group_8")
find_and_click_element_by_id(driver, "start_btn")


URL = 'https://covid19.ontariohealth.ca/'
driver.get(URL)
print(driver.title)

WebDriverWait(driver, 3)
#page 1 - Accept Terms
find_and_click_element_by_id(driver, "home_acceptTerm1_label")
find_and_click_element_by_id(driver, "continue_button")

WebDriverWait(driver, 3)
#Page 2 Enter Health Card Info
find_and_enter_data_in_text_box_by_id(driver, "hcn", "<<enter health card number>>")
find_and_enter_data_in_text_box_by_id(driver, "vcode", "<<enter health card version code>>")
find_and_enter_data_in_text_box_by_id(driver, "scn", "<<enter health card number on the back>>")
find_and_enter_data_in_text_box_by_id(driver, "dob", "<<enter date of birth>>")
find_and_enter_data_in_text_box_by_id(driver, "postal", "<<enter postal code>>")
find_and_click_element_by_id(driver, "continue_button")

WebDriverWait(driver, 3)
find_and_click_element_by_id(driver, "booking_button")

WebDriverWait(driver, 3)
find_and_click_element_by_id(driver, "fld_booking-home_interval_no_label")
find_and_click_element_by_id(driver, "second_dose_button")
#find_and_enter_data_in_text_box_by_id(driver, "location-search-address", "<<enter location>>")

elems = driver.find_elements_by_tag_name("button")
for elem in elems:
    buttondata = elem.get_attribute("class")
    if buttondata == 'tw-text-accent1 tw-underline focus:tw-outline-accent1' :
        if elem.text == 'Use your current location' :
            elem.click()
            passed=True
            break


find_and_click_element_by_id(driver, "second_dose_button")