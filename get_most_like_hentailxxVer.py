import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import pprint

import datetime

driver = webdriver.Edge(executable_path = r"\Users\boboi\Downloads\Compressed\edgedriver_win64\msedgedriver.exe")

driver.get("http://hentailxx.com/")
driver.get('http://hentailxx.com/story/index.php?p=1')

all_eng = []

today_date = datetime.date.today()
date_format = "%H:%M %d/%m/%Y"
today_time = today_date.strftime(date_format)
filename = "witl-" + "_vLxx.txt"

def process_newtab( link ):
	window_before = driver.window_handles[0]

	driver.execute_script("window.open('about:blank','_blank');")
	driver.switch_to.window(driver.window_handles[1])
	driver.get(link)
	
	checker = 0
	# /html/body/main/div/div[3]/div[1]/div/div[2]/text()[2]
	# /html/body/main/div/div[3]/div[1]/div/div[2]/text()[3]
	a = driver.find_element_by_xpath("/html/body/main/div/div[3]/div[1]/div/div[2]").text
	a = a.splitlines()	

	b = datetime.datetime.strptime(today_time, date_format)
	c = a[1]
	c = datetime.datetime.strptime(c, date_format)

	if b - c > datetime.timedelta(days=7) :
		checker = 1
	else:
		rawText = a[2]
		rawText = ''.join([n for n in rawText if n.isdigit()])
		print(c)
		print(rawText)
		all_eng.append( ( int(rawText), link ) )
		
	# print(rawText)
	# print(link)
	# print(driver.find_element_by_tag_name("time").text)

	driver.close()
	driver.switch_to.window(window_before)
	return checker

# items = "/html/body/main/div/div[3]/div[1]/div/div[" + str(index) + "]"
# 		xitems = driver.find_element_by_xpath(items)
# 		html = xitems.get_attribute('outerHTML')
# 		attrs = BeautifulSoup(html, 'html.parser').a.attrs
# 		print(attrs)

while True: #loop while 1-week past
	#get current index
	control_date = 0
	
	gallery = driver.find_elements_by_class_name("newestChapter")
	for img in gallery:
		try:
			control_date = process_newtab(img.find_element_by_css_selector('a').get_attribute('href'))
		except TimeoutException:
			continue
		if (control_date == 1):
			break;
	if (control_date == 1):
		break

	current_link = driver.current_url
	index_page = current_link[-1]
	index_page = int(index_page)+1
	current_link = current_link[:-1] + str(index_page)
	driver.get(current_link)

all_eng.sort(reverse = True)

# write

myfile = open(filename, 'w')

for item in all_eng:
	print(item[0])
	print(item[1])
	myfile.write(item[1])
	myfile.write("\n")

myfile.close()