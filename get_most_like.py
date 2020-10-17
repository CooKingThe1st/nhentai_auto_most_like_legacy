import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge(executable_path = r"\Users\boboi\Downloads\Compressed\edgedriver_win64\msedgedriver.exe")

driver.get('https://nhentai.net/search/?q=eng')

all_eng = []

def process_newtab( link ):
	window_before = driver.window_handles[0]

	driver.execute_script("window.open('about:blank','_blank');")
	driver.switch_to.window(driver.window_handles[1])
	driver.get(link)
	
	rawText = driver.find_element_by_class_name("nobold").text
	rawText = rawText[1:-1]

	checker = (driver.find_element_by_tag_name("time").text == "1 week ago")
	if (checker == False):
		all_eng.append( ( int(rawText), link ) )
	print(rawText)
	print(link)
	print(driver.find_element_by_tag_name("time").text)

	driver.close()
	driver.switch_to.window(window_before)
	return checker

while True: #loop while 1-week past
	#get current index
	control_date = 0

	gallery_list = driver.find_elements_by_class_name("cover")

	for img in gallery_list:
		control_date = process_newtab(img.get_attribute('href'))
		if (control_date == 1):
			break;
	if (control_date == 1):
		break

	driver.find_element_by_class_name("next").click()

all_eng.sort(reverse = True)

# write
from datetime import date

today = date.today()
filename = "witl-" + today.strftime("%b-%d-%Y") + ".txt"

myfile = open(filename, 'w')

for item in all_eng:
	print(item[0])
	print(item[1])
	myfile.write(item[1])
	myfile.write("\n")

myfile.close()