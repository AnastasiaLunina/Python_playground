from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

chrome_driver_path = Service(r"C:\Users\16314\Desktop\PROGRAMMING\_PROGRAMMS\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Click on links
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
article_count.click()

# Type in input
search = driver.find_element(By.NAME, 'search')
search.send_keys('Python')
# Hit Enter Key
search.send_keys(Keys.ENTER)

# driver.quit()