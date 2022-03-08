from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

s = Service("C:\development\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# number = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# number.click()

# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# all_portals.click()

# search_and_type = driver.find_element(By.CLASS_NAME, "vector-search-box-input").send_keys("Python" + Keys.ENTER)
def register():
    f_name = driver.find_element(By.NAME, "fName").send_keys("Edo")
    l_name = driver.find_element(By.NAME, "lName").send_keys("Rizvic")
    email = driver.find_element(By.NAME, "email").send_keys("edo@dummymail.com" + Keys.ENTER)
register()