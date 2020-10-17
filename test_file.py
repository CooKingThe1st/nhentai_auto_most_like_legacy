from datetime import date

today = date.today()
filename = "witl-" + today.strftime("%b-%d-%Y")

myfile = open(filename, 'w')

myfile.write('xxx')
myfile.close()