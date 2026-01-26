from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(20)
driver.get('http://uitestingplayground.com/ajax')

button = driver.find_element(By.CSS_SELECTOR, '#ajaxButton')
button.click()

txt = driver.find_element(By.CSS_SELECTOR, '[class="bg-success"]').text

print(f'"{txt}"')

driver.quit()
