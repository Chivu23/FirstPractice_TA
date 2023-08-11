# Exercitii Testare Automata

"""
1. Navigheaza catre urmatorul LINK: https://demo.nopcommerce.com/
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

link = 'https://demo.nopcommerce.com/'

driver.get(link)
time.sleep(2)

"""
2. Verifica ca titlul paginii este cel asteptat.
"""

# ---> accessarea titluli paginii curente

expected_title = 'nopCommerce demo store'
actual_title = driver.title
print(actual_title)

assert expected_title == actual_title


"""
3. Da click pe Register
"""

# ----> identificare dupa LINK TEXT

register_element = driver.find_element(By.LINK_TEXT, 'Register')
register_element.click()
time.sleep(3)

"""
4. Selecteaza un gen (sectiunea Gender).
Verifica ca elementul gasit are atributul type cu valoarea 'radio'
"""

# ----> identificare dupa ID

gender_input_element = driver.find_element(By.ID, 'gender-male')

# --->> verif atribute element HTML

assert gender_input_element.get_attribute('type') == 'radio'

gender_input_element.click()
time.sleep(3)


"""
5. Identifica elementul in care putem scrie prenumele.
Verifica ca elementul gasit are tag-ul corespunzator.
Scrie un prenume.
"""

#---> identif dupa  ID

FirstName_input_element = driver.find_element(By.ID, 'FirstName')

# --->>> verificare tag element

assert FirstName_input_element.tag_name == 'input'

FirstName_input_element.send_keys('George')
time.sleep(3)

"""
6. Identifica elementul in care putem scrie numele de familie.
Verifica ca elementul gasit are tag-ul corespunzator.
Scrie un nume de familie.
"""

last_name_element = driver.find_element(By.ID, 'LastName')

assert last_name_element.tag_name == 'input'

last_name_element.send_keys('Georgescu')
time.sleep(3)


"""
7. Identifica elementul in care putem scrie email-ul.
Verifica ca valoarea atributului name este cea asteptata.
Completeaza cu o adresa de email.
"""


email_element = driver.find_element(By.ID, 'Email')

# verif atribut element HTML
assert email_element.get_attribute('name') == 'Email'

email_element.send_keys('nustam@yahoo.com')
time.sleep(2)

"""
8. Identifica elementele in care trebuie sa introduci parolele
si introdu aceeasi parola (3 caractere) in ambele locuri.
Verifica ca apare mesajul de eroare asteptat.
"""

pwd_el = driver.find_element(By.ID, 'Password')
pwd_el.send_keys('123')

conf_pas_el = driver.find_element(By.ID, 'ConfirmPassword')
conf_pas_el.send_keys('123')

pwd_error_el = driver.find_element(By.ID, "Password-error")
actual_error_text = pwd_error_el.text
expected_error_text = 'Password must meet the following rules:\nmust have at least 6 characters'

assert actual_error_text == expected_error_text


# ------

"""
11. Inchide browser-ul.
"""
driver.quit()
