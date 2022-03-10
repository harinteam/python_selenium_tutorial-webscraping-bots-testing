# Selenium Tutorial #1


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
print(driver.title)

search = driver.find_element_by_name("s")
search.send_keys("python")
search.send_keys(Keys.RETURN)

print(driver.page_source)

time.sleep(5)

driver.quit()