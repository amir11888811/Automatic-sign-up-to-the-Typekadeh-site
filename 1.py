from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.ChromiumEdge()
driver.get("https://typekadeh.com")
btn=driver.find_element(By.CLASS_NAME,"close-button")
btn.click()
time.sleep(3)
btn=driver.find_element(By.CLASS_NAME,"tk-btn")
btn.click()
time.sleep(3)
btn=driver.find_elements(By.CLASS_NAME,"iranYekan-14--bold")
if len(btn)>1:
    btn=btn[1]
    btn.click()
time.sleep(3)
input=driver.find_elements(By.CLASS_NAME,"tk-input__dense")
time.sleep(1)
input[0].send_keys("you'r email")
time.sleep(2)
input[1].send_keys("you'r phone number")
time.sleep(2)
input[2].send_keys("username")
time.sleep(2)
input[3].send_keys("password")
time.sleep(2)
btn=driver.find_elements(By.CLASS_NAME,"tk-btn--primary")
btn[4].click()
time.sleep(20)