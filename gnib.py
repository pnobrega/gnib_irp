from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import configGNIB

driver = webdriver.Firefox()
driver.get('https://burghquayregistrationoffice.inis.gov.ie/Website/AMSREG/AMSRegWeb.nsf/AppSelect?OpenForm')
sleep(10)


driver.find_element_by_id('Category').send_keys("All")
sleep(1)

driver.find_element_by_id('SubCategory').send_keys("All")
sleep(1)

driver.find_element_by_id('ConfirmGNIB').send_keys("Yes")
sleep(1)

driver.find_element_by_id('GNIBNo').send_keys(configGNIB.noGNIB)
sleep(3)

GNIBExDT = driver.find_element_by_css_selector("input#GNIBExDT")
driver.execute_script("window.scrollBy(0, 400)")
driver.execute_script("arguments[0].removeAttribute('readonly')", GNIBExDT);
driver.find_element_by_css_selector("input#GNIBExDT").send_keys(configGNIB.date_exGNIB)
GNIBExDT.send_keys(Keys.RETURN)
sleep(3)

driver.find_element_by_id('UsrDeclaration').click()
sleep(1)

driver.find_element_by_id('GivenName').send_keys(configGNIB.name)
sleep(1)

driver.find_element_by_id('SurName').send_keys(configGNIB.lastName)
sleep(1)

dob = driver.find_element_by_css_selector("input#DOB")
driver.execute_script("window.scrollBy(0, 400)")
driver.execute_script("arguments[0].removeAttribute('readonly')", dob);
driver.find_element_by_css_selector("input#DOB").send_keys(configGNIB.dateOfBirth)
GNIBExDT.send_keys(Keys.RETURN)
sleep(3)

driver.find_element_by_id('Nationality').send_keys(configGNIB.Nationality)
sleep(1)

driver.find_element_by_id('Email').send_keys(configGNIB.EMAIL_ADDRESS)
sleep(1)

driver.find_element_by_id('EmailConfirm').send_keys(configGNIB.EMAIL_ADDRESS)
sleep(1)

driver.find_element_by_id('FamAppYN').send_keys("No")
sleep(1)

driver.find_element_by_id('PPNoYN').send_keys("Yes")
sleep(1)

driver.find_element_by_id('PPNo').send_keys(configGNIB.passportNo)
sleep(1)

driver.find_element_by_id('btLook4App').click()
sleep(1)

select = Select(driver.find_element_by_id('AppSelectChoice'))
select.select_by_value('S')
sleep(1)
driver.execute_script("window.scrollBy(0, 400)")
count=0
for x in range(0, 3):
    count=count+1
    print(count)
    if(count<45):            
        driver.find_element_by_id('btSrch4Apps').click()
        try:
            driver.find_element_by_xpath('/html/body/form/div/div[2]/div/div[3]/div[4]/div/div[1]/table/tbody/tr/td[1]/button').click()
        except:
            sleep(10)
#except: 
    #print('Error to connect to website')

#driver.quit()