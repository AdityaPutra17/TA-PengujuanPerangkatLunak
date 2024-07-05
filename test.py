from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# navigate ke orangehrm
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

##Login
#isi kolom username
username_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, 'username'))
)
username_input.send_keys('Admin')

#isi kolom password
password_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, 'password'))
)
password_input.send_keys('admin123')

#click login botton
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.TAG_NAME, 'button'))
)
login_button.click()

username_before_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'oxd-userdropdown-name'))
)
username_before = username_before_element.text
print("Username (Before): " + username_before)


##navigasi ke menu buzz
my_info_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, 'Buzz'))
)
my_info_link.click()

#add posting di buzz
add_post = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'oxd-buzz-post-input'))
)
add_post.send_keys('Haii..!! ini automation testing')
time.sleep(3)

#click button post
post_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'oxd-buzz-post-slot'))
)
post_button.click()

time.sleep(5)


##hapus postingan buzz
#click titik 3 di postingan
three_dots = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'bi-three-dots'))
)
three_dots.click()

#click menu delete
delete_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'bi-trash'))
)
delete_button.click()

#click confirm delete
confirm_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'oxd-button--label-danger'))
)
confirm_button.click()

time.sleep(10)

driver.refresh()

driver.quit()

