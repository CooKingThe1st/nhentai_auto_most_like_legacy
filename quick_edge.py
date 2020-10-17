import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge(executable_path = r"\Users\boboi\Downloads\Compressed\edgedriver_win64\msedgedriver.exe")

driver.get("https://www.popularmechanics.com/technology/robots/")