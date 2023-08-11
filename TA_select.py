from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# var easy

#driver = webdriver.Chrome()

# var recomadnata

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
time.sleep(5)

# --->  acces catre un link
driver.get('https://formy-project.herokuapp.com/form')
time.sleep(3)

# ---> maxim. wind.
driver.maximize_window()
time.sleep(2)

# SELECTOR BY ID

element = driver.find_element(By.ID, 'first-name')
print(element)
element.send_keys('CHIVU')
time.sleep(2)

# last_name_element = driver.find_element(By.ID, 'last.name')
# last_name_element.send_keys('CHiVOOO')
# time.sleep(2)

# print(last_name_element.tag_name)
# assert last_name_element.tag_name == 'input'
# time.sleep(1)
#
link_element = driver.find_element(By.LINK_TEXT, 'Submit')
link_element.click()
time.sleep(2)

#   --->> go back
driver.back()
time.sleep(2)

# PARTIAL LINK TEXT
link_element = driver.find_element(By.PARTIAL_LINK_TEXT, 'Sub')
link_element.click()
time.sleep(5)



