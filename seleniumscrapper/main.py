import items as items
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service("C:\development\chromedriver.exe")

driver = webdriver.Chrome(service=s)

driver.get("https://www.python.org/")
# # price = driver.find_element(By.CSS_SELECTOR,  ".a-text-price").text
# # print(price)
# # driver.close()
#
# price = driver.find_element(By.NAME,  "q")
# print(price.get_attribute('placeholder'))
upcoming_events = {}

dates= driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

for n in range(len(dates)):
    upcoming_events[n] = {
        "time": dates[n].text,
        "name": event_names[n].text,
    }

print(upcoming_events)
driver.quit()

