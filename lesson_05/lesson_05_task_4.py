from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

input_field = driver.find_element(By.ID, "username")
input_field.clear()
input_field.send_keys("tomsmith")
sleep(2)

input_field = driver.find_element(By.ID, "password")
input_field.clear()
input_field.send_keys("SuperSecretPassword!")
button = driver.find_element(By.CLASS_NAME, "fa")
button.click()
sleep(2)

flash_message = driver.find_element(By.CSS_SELECTOR, '#flash.flash.success')
text = flash_message.get_attribute('textContent').strip()
print(text[:-1])
driver.quit()
