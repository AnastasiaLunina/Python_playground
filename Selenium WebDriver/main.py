from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from pprint import pprint

chrome_driver_path = Service(r"C:\Users\16314\Desktop\PROGRAMMING\_PROGRAMMS\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

pprint(events)


driver.quit()