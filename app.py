from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
import time

driver = webdriver.Chrome()

driver.maximize_window()

URL = "https://google.com"
driver.get(URL)

driver.find_element_by_name("q").send_keys("Cyberpunk")
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)

time.sleep(5)

driver.close()

print("Test completed")