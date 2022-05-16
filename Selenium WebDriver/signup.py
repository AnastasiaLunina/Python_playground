from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

chrome_driver_path = Service(r"C:\Users\16314\Desktop\PROGRAMMING\_PROGRAMMS\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")

search = driver.find_element(By.NAME, 'fName')
search.send_keys('Anastasia')

search = driver.find_element(By.NAME, 'lName')
search.send_keys('Anastasia')

search = driver.find_element(By.NAME, 'email')
search.send_keys('aaa@bbb.ccc')

search.send_keys(Keys.ENTER)
