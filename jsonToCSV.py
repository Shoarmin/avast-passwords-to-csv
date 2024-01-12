# Python program to convert
# JSON file to CSV
import json
import csv
from collections import OrderedDict

# Get name of the passwords file
user_input = input("What is the name of your password file (dont include the file extension): ")

# Opening JSON file and loading the data
# into the variable data
with open(f'{user_input}.json') as json_file:
	data = json.load(json_file)

pswd_data = data['logins']

# now we will open a file for writing
data_file = open('pswd.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing 
# headers to the CSV file
count = 0

for pswd in pswd_data:
	if count == 0:

		# Writing headers of CSV file
		updated_dict = OrderedDict(("password" if key == "pwd" else key, value) for key, value in pswd.items())
		header = list(pswd.keys())
		index_to_replace_pwd, index_to_replace_login = header.index('pwd'), header.index('loginName')
		header[index_to_replace_pwd], header[index_to_replace_login]= 'password', 'login'
		csv_writer.writerow(header)
		count += 1

	# Writing data of CSV file
	csv_writer.writerow(pswd.values())

data_file.close()
