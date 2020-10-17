import re

f = open("witl-May-08-2020", "r")
fw = open("witl-May-09-2020.txt", "w")

str_all = f.read()
code_all = re.findall(r'\d+', str_all)
# print(code_all)
for code in code_all:
	link = "nhentai.net/g/" + code
	print(link)
	fw.write(link)
	fw.write("\n")
fw.close()
