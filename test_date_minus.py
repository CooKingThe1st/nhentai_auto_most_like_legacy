import datetime
date_format = "%H:%M %m/%d/%Y"
a = datetime.datetime.strptime('20:58 8/18/2008', date_format)
b = datetime.datetime.strptime('21:58 9/26/2008', date_format)
delta = b - a
print (delta.days) # that's it

if delta > datetime.timedelta(days=12):
	print("allejfasdf")