#! python3
# platform = Ubuntu
# regexSearch.py - searches for the word or lines from the text files.

import re
import sys
import os

# For decoration on the shell
# Includes colors, fonts, sizes
BLUE, RED, WHITE, YELLOW, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[32m', '\033[0m'

if len(sys.argv) < 2:
    sys.stdout.write(GREEN + """    
   ▄████████    ▄████████    ▄████████    ▄████████  ▄████████    ▄█    █▄    
  ███    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███   
  ███    █▀    ███    █▀    ███    ███   ███    ███ ███    █▀    ███    ███   
  ███         ▄███▄▄▄       ███    ███  ▄███▄▄▄▄██▀ ███         ▄███▄▄▄▄███▄▄ 
▀███████████ ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀▀▀   ███        ▀▀███▀▀▀▀███▀  
         ███   ███    █▄    ███    ███ ▀███████████ ███    █▄    ███    ███   
   ▄█    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███   
 ▄████████▀    ██████████   ███    █▀    ███    ███ ████████▀    ███    █▀    
                                         ███    ███                                                                                                                      
    """  + END + BLUE +
    '\n' + 'Matching String Finder'.format(RED, END).center(69) +
    '\n' + 'Made ^_^ by: {}NUMB | NIRAJ'.format(YELLOW, RED, YELLOW, BLUE).center(76) +
    '\n' + 'Version: {}1.0{}\n'.format(YELLOW, END).center(80) + '\n')
else:
    sys.exit('Usage: python3 regexSearch.py')
    os.system("clear")


################# THIS PROGRAM COULD BE DONE IN TWO WAYS ######################
# If you know how many text files are there in your folder and their name too. Go for program => 1.
# If you dont have any idea about the number of files and their name. Go for program => 2.
#################################################################################

# PROGRAM 1
# Word or line the user want to search to the files
word = input("     [+] Enter the word or line you want to search: ")

# First open the file test1.txt and search on it.
with open('test1.txt') as file1:
	data1 = file1.read()
	finded = re.compile(word)
	final = finded.search(data1)

	try:
		print("\n     [+] Result found in 'test1.txt' : {}".format(final.group()))

	# If the line or word is not found, open second file test2.txt
	except:
		with open('test2.txt') as file2:
			data2 = file2.read()
			finded2 = re.compile(word)
			final2 = finded2.search(data2)

		try:
			print("\n     [+] Result found in 'test2.txt' : {}".format(final2.group()))

		# If the line or word is not found again, open thrid file test3.txt
		except:
			with open('test3.txt') as file3:
				data3 = file3.read()
				finded3 = re.compile(word)
				final3 = finded3.search(data3)

			try:
				print("\n     [+] Result found in 'test2.txt' : {}".format(final3.group()))

			# If it does not find at any file, print error messages.
			except:
				print("\n     [+] Result not found!!")



# PROGRAM 2
# Create an empty list and counter as 0
fileList = []
counter = 0
word = input("\n     [+] Enter word or line you want to search: ")

# Loop through each files on the current working directory.
for filename in os.listdir(os.getcwd()):
	try: 
		# Open each file and search for the text files.
		textfile = re.compile(r'\w*.txt')
		finalfile = textfile.search(filename)

		# If the regex matches then append each text file to the list.
		fileList.append(finalfile.group())
	except:
		pass

# Loop through each text files on the list.
# Open each file and search for the word or line given by the user.
for each_file in fileList:
	with open(each_file) as file2:
			data2 = file2.read()
			finded2 = re.compile(word)
			final2 = finded2.search(data2)

	try:
		print("\n     [+] Result found in '{0}' : {1}".format(each_file, final2.group()))
		print('\n')

	# If the line or word is not found increase the counter value by 1.
	except:
		counter += 1

# This condition means if the word is found in any file than counter value will not be equal to 
# the length of the list, i.e number of text files in the folder.
# So this condition satisfy only if no any word or line is matched on the files.
if counter == len(fileList):
	print('\nResult not found!!\n')