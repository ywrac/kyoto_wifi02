from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from passcodes import CODE

driver = webdriver.Firefox()
driver.get('https://login.inf-kyoto-city.info/')
form = driver.find_element_by_tag_name('form')
passcode = form.find_element_by_id('passcode')
passcode.send_keys(CODE)
form.submit()
