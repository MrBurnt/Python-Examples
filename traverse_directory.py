#! python3
import os

for folder_name, subfolder, file_names in os.walk(r'C:\Users\rashi\Pictures'):
	print('In folder: ' + folder_name + ' is:')
	print('These folders: ' + str(subfolder))
	print('These files: ' + str(file_names))
	print('These files: ' + str(file_names))