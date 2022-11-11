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

# Part 1: Data Loading
# ***********************************************************

file = open('2019_Airline_Delays_Dataset_train.csv')
type(file)

csvreader = csv.reader(file, delimiter=',')

header = []
header = next(csvreader)
print(f'The columns names are {", ".join(header)}')

rows = []
for row in csvreader:
        rows.append(row)
print(rows)

file.close()

# Part 2: Exploring the Data
# ***********************************************************

# Part 3: Describing the Data
# ***********************************************************

# Part 4: Analysis
# ***********************************************************

# Part 5: Interface
# ***********************************************************
