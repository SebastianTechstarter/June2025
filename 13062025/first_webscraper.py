from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

user_input = input("Von welcher Wikipedia Seite möchtest du die Bilder scrapen ?: ")
driver = webdriver.Chrome()

driver.get("https://www.wikipedia.de")
search_field = driver.find_element(By.ID, "txtSearch")
search_field.send_keys(user_input)
search_field.send_keys(Keys.RETURN)

img_sources = [
    img.get_attribute("src") for img in driver.find_elements(By.TAG_NAME, "img")
]
with open("first_webscraper.txt", "a") as file:
    for img_source in img_sources:
        file.write(img_source + "\n")

driver.quit()
