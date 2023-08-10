from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, 'cookie')

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout_start = time.time()
timeout = time.time() + 5
session = time.time() + 60 * 5

while True:
    cookie.click()
    if time.time() > timeout:
        store = driver.find_elements(By.CSS_SELECTOR, '#store b')
        item_prices = []
        for item in store:
            element_text = item.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        money = int(driver.find_element(By.ID, 'money').text)
        # print(money.text)
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if money > cost:
                affordable_upgrades[cost] = id

        highest_price_affordable_upgrade = max(affordable_upgrades)
        # print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()

        timeout = time.time() + 5

    if time.time() > session:
        cookie_per_s = driver.find_element(By.ID,"cps").text
        print(cookie_per_s)
        break

driver.quit()
