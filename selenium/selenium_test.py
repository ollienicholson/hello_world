# First selenium test

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chrome_options = Options()

chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=chrome_options)

driver = webdriver.Chrome("C:/Users/olive/Documents/GitHub/tutorials/selenium/chromedriver.exe", options= chrome_options)
driver.get("https://www.python.org")

# driver.get("https://worldathletics.org/athletes-home")
# driver.find_elements(by=By.CLASS_NAME,value="SearchForm_searchField__10my7")
# driver.find_element(by=By.CLASS_NAME,value="SearchForm_searchIcon__3Hj1Y").send_keys(Keys.ENTER)
# driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver/", options=chrome_options)

# 14257893

print(driver.title)

search_bar = driver.find_element(by=By.ID, value="q")

print("done")

search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)

# def selenium_chrome(url):
#     browser = webdriver.Chrome()
#     browser.get(url)
#     return browser

# selenium_chrome("https://www.python.org")

"C:/Users/olive/Documents/GitHub/tutorials/selenium/chromedriver.exe"
