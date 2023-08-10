from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.python.org")
events = driver.find_element(By.XPATH,'//*[@id="content"]/div/section/div[2]/div[2]/div/ul').text.splitlines()
print(events)
dictionary = { i: {'time': events[i], 'name': events[i+1]} for i in range(0, len(events), 2)}
print(dictionary)

driver.quit()