#! /usr/bin/python3 -s

import sys

# from calendar import monthrange as monthrange
import datetime as dt

# import time
# from datetime import datetime
# from calendar import monthrange
# int(time.mktime(datetime.now().timetuple()))

text = open(sys.argv[1], "r")

dates = []
start_url_number = 0
basic_url = []

for line in text:
	if line[0] == "#":
		pass
	else:
		line = line.replace('\n', '')
		alt_line = line.split("\t")

		clean_line = []
		for cad in alt_line:
			if cad == '':
				pass
			else:
				clean_line += [cad]

		if clean_line != []:
			[date, url] = [clean_line[0], clean_line[-1]]

			dates.append(date)
			
			if start_url_number == 0:
				alt_url = url.split('/')

				basic_url = url.split('/day')

				basic_url[0] += "/day"
				basic_url[1] = basic_url[1][-4:]

				# print(basic_url)

				start_url_number = int(alt_url[-1][3:-4])

				# print(start_url_number)

			# print(date, '\t', url)
		else:
			pass

print (dates)
print (start_url_number)
print (basic_url)

dates_dated = []

first_time = True

total_samples = 0

for date_str in dates:
	crry_date = date_str.split("-")

	year = int(crry_date[0])
	month = int(crry_date[1])
	day = int(crry_date[2]) 
	
	# print(dt.date(year, month, day))

	dates_dated.append(dt.date(year, month, day))

	print("Date \t :", dates_dated[-1])

	# print("\t\tTO DATE\t:")

	if first_time:
		pass
	else:
		print("Samples \t\t::")
		print((dates_dated[-1] - dates_dated[-2]).days)

		total_samples += (dates_dated[-1] - dates_dated[-2]).days

	print("\n")
	first_time = False

print("TOTAL SAMPLES\t", total_samples)