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
        
        #time start
        tic = time.perf_counter()
        
        #reads the file and stores it in a dataframe
        self.data = pd.read_csv(filenames[user_input])
        
        #time ends
        toc = time.perf_counter()
        print(f"Loaded file in {toc - tic:0.4f} seconds")
        
        #gets the column names and stores them in a list
        self.col_names = list(self.data.columns)
        
    def search_functionality(self):
        #ask user input for search
        #user_input = str(input("\nEnter anything to search data\n"))
        print("Searching Value in Data")
    
        
    def explore_data (self):
        # testing function 
        # modify according to website requirements
        self.search_functionality()
        print(self.data.head(5))
        
    
        

    def describe_data(self):
        # testing function 
        # modify according to website requirements
        print(self.data.head(10))
        
    def analyze_data (self):
        # testing function 
        # modify according to website requirements
        print(self.data.head(15))
        
    # Function to retrieve the total amount of delays experience by all carriers 
    '''def total_delays(self):
        total_delays = 0
        for row in self.rows:
            if (int(row.depart_delay) == 1):
                total_delays = total_delays + 1
        return total_delays

    # function used to answer question 3&4 of the analysis question
    def Alex_analysis(self):
        # Create an array containing the unique names of every carrier
        carriers = []
        for row in self.rows:
            if (row.carrier_name not in carriers):
                carriers.append(row.carrier_name)
        
        # Create an array containg the number of delays for each carrier
        # example: American Airlines Inc. = carriers[0]
        #          number of delays for American Airlines Inc. = delays[0]
        # Put this in a seperate for loop since we dont know how many 
        # aircraft carriers are in the csv file
        delays = [0] * len(carriers)
        planeAge = 0
        for row in self.rows:        
            if (int(row.depart_delay) == 1): 
                # Find the average plane age for every american Airline plane delayed
                if (row.carrier_name == 'American Airlines Inc.'):
                    planeAge = planeAge + int(row.plane_age)

                count = 0 
                for elements in carriers:
                    # Find the aircraft carrier with the most delays in july,
                    # january, and december
                    if(carriers[count] == row.carrier_name):
                        if (int(row.month) == 1):
                            delays[count] = delays[count] + 1
                        elif (int(row.month) == 7):
                            delays[count] = delays[count] + 1
                        elif (int(row.month) == 12):
                            delays[count] = delays[count] + 1
                    count = count + 1

        count = 0
        most_delays = 0;
        for i in range(len(delays)):
            if (most_delays < delays[i]):
                most_delays = delays[i]
                count = i

        print("\nThe airline carrier that expereinced the most delays in January, July, and December was: "f'{carriers[count]}')
        print("with " ,most_delays, " delays")
        avg_age = planeAge/delays[0]
        print("\nThe average plane age of all planes with delays operated by American Airlines is: ", avg_age)
        # Test Prints to make sure data gatrhered was correct       
        # print('names of different carriers\n ',carriers)
        # print('amount of different aircraft carriers: ',len(carriers))
        # print(delays)
        
    # Print the data.
    def print_data(self):
        user_input = int(input("\nEnter the number of rows you want to print out\n"))
        count = 1
        pp = pprint.PrettyPrinter(sort_dicts = False)
        for row in islice(self.rows,0, user_input): 
            print('Row number: ' + str(count))
            # print(f'{row.month}/{row.day} {row.carrier_name}')
            # print(f'{row.month}/{row.day}')
            # print(f' departure delay {row.depart_delay}')
            print(f"""{'-'*20}
month & day     | {row.month}/{row.day}
Carrier name    | {row.carrier_name}
departure delay | {row.depart_delay}
departure time  | {row.depart_time}
distance group  | {row.distance_group}
segment number  | {row.seg_num}
{'-'*20}
                """)
            count = count + 1'''


def main():
    input_flag = True
    # Load the data.
    data = Data()
    data.load_data()
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
            data.explore_data()
        if user_input == '2':
            data.describe_data()
        if user_input == '3':
            data.analyze_data()
        if user_input == '4':
            data.load_data()
        if (user_input == 'q') or (user_input == 'Q') :
            input_flag = False
            break
# Print the data.
#print("Part 4 the analaysis questions")
#d.Alex_analysis()
# d.print_data()
if __name__ == "__main__":
    main()