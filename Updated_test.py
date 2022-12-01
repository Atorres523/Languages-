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
import pprint
import pandas as pd
import time
# Define a class to hold an individual row of data from the CSV file.
# each row will correspond to its own object

# global variable
def find_csv_filenames(path_to_dir, suffix=".csv" ):
        filenames = listdir(path_to_dir)
        return [ filename for filename in filenames if filename.endswith(suffix) ]


    
# Define a class to hold data from the CSV file.
class Data:
    def __init__(self):
        # this list holds all the Row objects created
        # Row[0] contains an object. That object contains the value in every 
        #  column of that row
        self.col_names = []
        self.data = []
        #self.list_data = []

    # Load data from a CSV file.
    def load_data(self):    
        # gets directory csv filenames
        count = 0
        dir_path = str(os.getcwd() + "/")
        filenames = find_csv_filenames(dir_path)
        print("Here are a list of the CSV Files found:\n")
        for name in filenames:
                print("%s: %s" % (str(count), name))
                count += 1
        # ask for user input for which file to use
        user_input = int(input("\nEnter the number of the file you wish to use\n"))
        # time start
        tic = time.perf_counter()
        # reads the file and stores it in a dataframe
        try:
           self.data = pd.read_csv(filenames[user_input])
           toc = time.perf_counter()
           print(f"Loaded file in {toc - tic:0.4f} seconds")
        except:
            print("An error happened when loading the file")
            main()
        # time ends
        # toc = time.perf_counter()
        # print(f"Loaded file in {toc - tic:0.4f} seconds")
        # gets the column names and stores them in a list
        #self.col_names = list(self.data.columns)
        # get dataframe and store in a list
        #self.list_data = self.data.values.tolist()
        
    def search_functionality(self):
        #ask user input for search
        print("Searching Value in Data")
        user_input = str(input("\nEnter anything to search data\n"))
        user_input_int = int(user_input)
        print("Filtered Value in Data Based on Search Values")
        print("As an integer value")
        print(self.data[self.data.eq(user_input_int).any(1)])
        print("As a string value")
        print(self.data[self.data.eq(user_input).any(1)])
    def print_data(self):
        user_input = int(input("\nEnter the number of rows you want to print out (up to 5000):\n"))    
        print(self.data.head(user_input))
        #self.distinct_column_values()
        
    def distinct_column_values(self):
        #need to fix invalid input error
        # Count distinct values of any column selected by the user
        #unique_items = set(self.data.head)
        #keys = [[entry[0] for entry in unique_items]]
        #for key in set(keys):
         #   print("Key '{}' appears {} unique times".format(key, keys.count(key)))

        user_input = str(input("\nEnter a Column name to show unique values (e.g. 'PREVIOUS_AIRPORT')\n"))
        #print(self.col_names)
        get_count = self.data.pivot_table(columns=[user_input], aggfunc='size')
        print(get_count)


    def explore_data (self):
        # testing function 
        # modify according to website requirements
        
        # Requirements:
        # list all columns in the dataset and offer the user the possibility of drop any of them
        # Count distinct values of any column selected by the user                                      COMPLETED by Ed
        # Search any value in any column as input by the user                                           COMPLETED by Esmeralda
        # Sort any columns (Ascending or descending) as selected by the user
        # Print the first 100, 1000 or 5000 rows of the dataset as selected by the user                 COMPLETED by Alex and Esmeralda
        
        self.search_functionality()
        print("--------------------------------------------------")
        self.print_data()
        print("--------------------------------------------------")
      
    def count_function(self):
        print("Count the number of rows and columns")
        list_data = self.data.values.tolist()
        number = []
        number.append(len(list_data))       #rows = number[0]
        number.append(len(list_data[0]))    #columns = number[1]
        return number

    def describe_data(self):
        # testing function 
        # modify according to website requirements
        
        # Requirements:
        # Count                         COMPLETED by Esmeralda
        # Unique    
        # Mean                          Esmeralda
        # Median                        Esmeralda
        # Mode
        # Standard Deviation (SD)
        # Variance
        # Minimum
        # Maximum
        # 20 Percentile (P20)           
        # 40 Percentile (P40)
        # 50 Percentile (P50)
        # 60 Percentile (P60)
        # 80 Percentile (P80)
        numbers = []
        numbers = self.count_function()
        print("Number of rows: ", numbers[0])
        print("Number of columns: ", numbers[1])
        
    def analyze_data (self):

        
        # testing function 
        # modify according to website requirements
        
        # Requirements:
        # How many airlines are included in the data set? Print the first 5 in alphabetical order.                                          Ed                                          Ed
        # How many departing airports are included in the data set? Print the last 5 in alphabetical order.                                 Esmeralda 
        # What airline has the oldest plane?
        # What was the greatest delay ever recorded? print the airline and airpots of this event.                                           Alex
        # What was the smallest delay ever recorded? print the airline and airports of this event.                                          Alex
        # What was the month of the year in 2019 with most delays overall? And how many delays were recorded in that month?                 Esmeralda
        # What was the month of the year in 2019 with most delays overall? And how many delays were recorded in that day?                   Esmeralda
        # What airline carrier experience the most delays in January, July and December                                                     Alex
        # What was the average plane age of all planes with delays operated by American Airlines inc.                                       Alex
        # How many planes were delayed for more than 15 minutes during days with "heavy snow" (Days when the inches of snow on ground were 15 or more) )?   Ed
        # What are the 5 airports (Deaprting Airpots) that had the most delays in 2019? Print the airports and the number of delays         Ed
        self.Alex_analysis()
        self.ed_analysis()
        print("--------------------------------------------------")
        print(self.data.head(15))
        
    def Alex_analysis (self):
        num_months = [1,7,12]
        months = ['January', 'July', 'December']
        count = 0
        print("\n8. What airline carrier experience the most delays in January, July and December?")
        for i in num_months:
            filt = (self.data['MONTH'] == i) & (self.data['DEP_DEL15'] == 1)    
            temp = self.data.loc[filt, 'CARRIER_NAME'].values.tolist()
            #print(temp)
            # Create a dictionary key = carrier name, value = number of delays 
            carrierDelays = {}
            for j in temp:
                if not j in carrierDelays:
                    carrierDelays[j] = 1
                else:
                    carrierDelays[j] += 1
            #print(carrierDelays)
            
            #Find the max number of delays in the dictionary
            max_delays_carriers = []
            delays = 0
            for key,value in carrierDelays.items():
                if (delays <= value):
                    delays = value
            # Get the name of the carrier/s htt experienced the most delays
            for key,value in carrierDelays.items():
                if (delays == value):
                    max_delays_carriers.append(key)

            #print out the result to answer the question
            print(months[count], end = ": ")
            if (len(max_delays_carriers) > 1):
                print("Max number of delays was:", delays, "by both:", end = " ")
                for j in range(len(max_delays_carriers)):
                    print(max_delays_carriers[j], end = " ")
                print()
            else:
                print("Max number of delays was:", delays, "by: ", max_delays_carriers[0])
            count += 1
        
        #Analysis Question 9
        filt = (self.data['CARRIER_NAME'] == 'American Airlines Inc.') & (self.data['DEP_DEL15'] == 1)
        planeAges = self.data.loc[filt, 'PLANE_AGE'].values.tolist()
        avg_plane_age = 0;
        for i in range(len(planeAges)):
            avg_plane_age = avg_plane_age + planeAges[i]
        avg_plane_age = avg_plane_age / len(planeAges)
        print("\n9. What was the average plane age of all planes with delays operated by American Airlines inc.?")
        print("The average plane age of American Airlines inc. which had delays was:",int(avg_plane_age), "years old")

    def ed_analysis (self):
        #analysis 1
        # How many airlines are included in the data set? Print the first 5 in alphabetical order.
        print("\nNumber of airlines in the data set: \n")
        num_airlines = len(set(self.data))
        print (num_airlines)
        print("--------------------------------------------------")

        print("\nFirst 5 airlines in alphabetical: \n") 
        temp = self.data['CARRIER_NAME'].values.tolist()
        unique_airlines = []
        for word in temp:
            if word not in unique_airlines:
                unique_airlines.append(word)
        unique_airlines.sort()
        temp = unique_airlines
        print (temp[0])
        for i in range(4):
            print(temp[i])
        

def main():
    input_flag = True
    # Load the data.
    d = Data()
    d.load_data()
    while input_flag:
        print("")
        print("Menu")
        print("--------------------------------------------------")
        print(" 1. Explore Data")    
        print(" 2. Describe Data")
        print(" 3. Analyze Data") 
        print(" 4. Load Different Data")
        print(" q. Quit Program")   
        print("--------------------------------------------------")
        user_input = str(input("\nEnter the number/character from the menu\n"))
        if user_input == '1':
            d.explore_data()
        if user_input == '2':
            d.describe_data()
        if user_input == '3':
            d.analyze_data()
        if user_input == '4':
            d.load_data()
        if (user_input == 'q') or (user_input == 'Q') :
            input_flag = False
            break
# Print the data.
#print("Part 4 the analaysis questions")
#d.Alex_analysis()
# d.print_data()
if __name__ == "__main__":
    main()
