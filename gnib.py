from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

#GNIBDATE = input('GNIB date: ')
driver = webdriver.Firefox()
driver.get('https://burghquayregistrationoffice.inis.gov.ie/Website/AMSREG/AMSRegWeb.nsf/AppSelect?OpenForm')
sleep(30)

driver.find_element_by_id('Category').send_keys("All")
sleep(1)

driver.find_element_by_id('SubCategory').send_keys("All")
sleep(1)

driver.find_element_by_id('ConfirmGNIB').send_keys("Yes")
sleep(1)

driver.find_element_by_id('GNIBNo').send_keys("123456")
sleep(3)

GNIBExDT = driver.find_element_by_css_selector("input#GNIBExDT")
driver.execute_script("window.scrollBy(0, 400)")
driver.execute_script("arguments[0].removeAttribute('readonly')", GNIBExDT);
driver.find_element_by_css_selector("input#GNIBExDT").send_keys("15/08/2019")
GNIBExDT.send_keys(Keys.RETURN)
sleep(3)

driver.find_element_by_id('UsrDeclaration').click()
sleep(1)

driver.find_element_by_id('GivenName').send_keys("Paul")
sleep(1)

driver.find_element_by_id('SurName').send_keys("Nobrega")
sleep(1)

dob = driver.find_element_by_css_selector("input#DOB")
driver.execute_script("window.scrollBy(0, 400)")
driver.execute_script("arguments[0].removeAttribute('readonly')", dob);
driver.find_element_by_css_selector("input#DOB").send_keys("10/08/1987")
GNIBExDT.send_keys(Keys.RETURN)

driver.find_element_by_id('Nationality').send_keys("Brazil")
sleep(1)

driver.find_element_by_id('Email').send_keys("email@gmail.com")
sleep(1)

driver.find_element_by_id('EmailConfirm').send_keys("email@gmail.com")
sleep(1)

driver.find_element_by_id('FamAppYN').send_keys("No")
sleep(1)

driver.find_element_by_id('PPNoYN').send_keys("Yes")
sleep(1)

driver.find_element_by_id('PPNo').send_keys("AA123456")
sleep(1)

driver.find_element_by_id('btLook4App').click()
sleep(1)

select = Select(driver.find_element_by_id('AppSelectChoice'))
select.select_by_value('S')
sleep(1)
driver.execute_script("window.scrollBy(0, 400)")

driver.find_element_by_id('btSrch4Apps').click()
sleep(1)

driver.quit()