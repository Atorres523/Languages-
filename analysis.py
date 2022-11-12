"""
# course: cmps3500
# CLASS Project
# PYTHON IMPLEMENTATION: BASIC DATA ANALYSIS
# date: 09/10/09
# Student 1: Alexis Torres
# Student 2: Esmeralda Osornio
# Student 3: Miguel Bueno Nunez
# Student 4: Edward Kyles
# description: Implementation Basic Data Analysys Routines
"""

import csv
import os
from os import listdir
from itertools import islice

# Part 1: Data Loading
# ***********************************************************

# finds all .csv files within the directory 
def find_csv_filenames(path_to_dir, suffix=".csv" ):
        filenames = listdir(path_to_dir)
        return [ filename for filename in filenames if filename.endswith(suffix) ]

# testing for path in
#print(os.getcwd())

# gets directory
dir_path = str(os.getcwd() + "/")

# checking if using the correct path
#print(dir_path)

filenames = find_csv_filenames(dir_path)


count = 0
print("Here are a list of the CSV Files found:\n")
for name in filenames:
        print("%s: %s" % (str(count), name))
        count += 1

user_input = int(input("\nEnter the number of the file you wish to use\n"))

# testing to see if user_input worked
#print(filenames[user_input])


# opens the file
file = open(filenames[user_input])
type(file)

# reads the file and saves it into csvreader
csvreader = csv.reader(file, delimiter=',')

# list all of the header
header = []
header = next(csvreader)
print(f'\nThe columns names are {", ".join(header)}')

# Print out a user specified number of unformated rows
# Rows are printed out one-by-one as a list  
user_input = int(input("\nEnter the number of rows you want to print out\n"))
for row in islice(csvreader,0,user_input):
        print(row)

# list all the rows unformatted
# rows = []
# for row in csvreader:
#         rows.append(row)
# print(rows)

file.close()

# Part 2: Exploring the Data
# ***********************************************************

# Part 3: Describing the Data
# ***********************************************************

# Part 4: Analysis
# ***********************************************************

# Part 5: Interface
# ***********************************************************
