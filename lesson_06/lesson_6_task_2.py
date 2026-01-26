from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(20)
driver.get('http://uitestingplayground.com/textinput')

element = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
element.clear()
element.send_keys('SkyPro')
button = driver.find_element(By.CSS_SELECTOR, '#updatingButton')
button.click()

txt = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text

print(f'"{txt}"')

driver.quit()
