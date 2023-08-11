# Exercise

"""
1.
- Instantiaza un browser de Chrome.
- Acceseaza pagina https://the-internet.herokuapp.com/
- Maximizeaza fereastra
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

import time

link = 'https://the-internet.herokuapp.com/'

driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)

driver.maximize_window()
time.sleep(2)


"""
2. Acceseaza link-ul Form Authentication, folosind un selector potrivit.
Incearca mai multe variante posibile.
"""

link_element = driver.find_element(By.PARTIAL_LINK_TEXT, 'Form')
link_element.click()
time.sleep(2)

# link_element = driver.find_element(By.LINK_TEXT, 'Form Authentication')
# link_element.click()
# time.sleep(3)


"""
3. Identifica elementul ce contine textul "Login Page"
si verifica, folosind un assert, ca acest element are textul asteptat
"""

# >>>link.element<<<  (aici cred ca i ceva not ok) = driver.find_element(By.LINK_TEXT, "Login Page")
#
# actual_text = link_element.text
# expected_text = 'Login Page'
#
# assert actual_text == expected_text
login_text = driver.find_element(By.TAG_NAME, 'h2')
login_button = driver.find_element(By.CLASS_NAME, 'radius')
assert login_text.text == "Login Page"
time.sleep(2)


"""
4. Identifica input-urile username si password,
introdu valori valide, si da click pe butonul login
"""

# username_input_element = driver.find_element(By.ID, 'username')
# assert username_input_element.tag_name == 'input'
#
# username_input_element.send_keys('tomsmith')
# time.sleep(2)
#
# password_input_element = driver.find_element(By.ID, 'password')
# assert password_input_element.tag_name == 'input'
#
# password_input_element.send_keys('SuperSecretPassword!')
#
# click_link_element = driver.find_element(By.LINK_TEXT, 'Login')
# click_link_element.click()
# time.sleep(3)

"""
5. Verifica, folosind un assert ca ai ajuns pe pagina
https://the-internet.herokuapp.com/secure
"""

# url = 'https://the-internet.herokuapp.com/secure'
# assert driver.current_url == 'https://the-internet.herokuapp.com/secure'


"""
6. Da click pe butonul logout
"""
#
# logout2 = driver.find_element(By.LINK_TEXT, "Logout")
# logout2 = driver.find_element(By.CLASS_NAME, "button.secondary.radius") # corect
# logout2.click()

logout2 = driver.find_element(By.CLASS_NAME, "button.secondary.radius")  # corect
logout2.click()


"""
7. Introdu un username corect si o parola incorecta.
Identifica mesajul care apare si verifica in cod ca acela este mesajul asteptat.
"""

username_input_element = driver.find_element(By.ID, 'username')
username_input_element.send_keys('tomsmith')

password_input_element = driver.find_element(By.ID, 'password')
password_input_element.send_keys('123')

login_btn = driver.find_element(By.CLASS_NAME, "radius")
login_btn.click()


error_elem = driver.find_element(By.ID, 'flash')
print(error_elem)

# var. 1

# expected
expected_error = 'Your password is invalid!\n'
assert expected_error == error_elem.text


#var. 2

assert 'Your password is invalid!' in error_elem.text


"""
8. Introdu un username corect.
Gaseste elementul cu tag-ul h4.
Ia textul de pe el si fa split dupa spatiu. Considera fiecare cuvant ca o potentiala parola.
Foloseste o structura iterativa prin care sa introduci rand pe rand parolele si sa apesi login
La final, testul trebuie sa printeze fie "Nu am reusit sa gasesc parola", fie "Parola secreta este 
[parola]"
"""

# text = "this is a text"
# print(text.split())

h4_elem = driver.find_element(By.TAG_NAME, "h4")
posib_pass = h4_elem.text.split()
print(posib_pass)

posib_pass[16] = 'parolaincorecta'
print(posib_pass)

for pwd in posib_pass:
    username_input_element = driver.find_element(By.ID, 'username')
    username_input_element.send_keys('tomsmith')
    password_input_element = driver.find_element(By.ID, 'password')
    password_input_element.send_keys(pwd)

    btn = driver.find_element(By.CLASS_NAME, 'radius')
    btn.click()
    if  driver.current_url == 'https://the-internet.herokuapp.com/secure':
        print(f'Parola secreta este {pwd}')
        break
else:
    print('Nu am reusit sagasesc parola')
