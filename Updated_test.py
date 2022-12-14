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
import datetime
# Define a class to hold an individual row of data from the CSV file.
# each row will correspond to its own object

# global variable
def find_csv_filenames(path_to_dir, suffix=".csv" ):
        filenames = listdir(path_to_dir)
        return [ filename for filename in filenames if filename.endswith(suffix) ]


    
# Define a class to hold data from the CSV file.
class Data:
    def __init__(self):
        self.data = []

    # Load data from a CSV file.
    def load_data(self):    
        # gets directory csv filenames
        count = 0
        dir_path = str(os.getcwd() + "/")
        filenames = find_csv_filenames(dir_path)
        print("\nHere are a list of the CSV Files found:\n")
        for name in filenames:
                print("%s: %s" % (str(count), name))
                count += 1
        try:
            # ask for user input for which file to use
            user_input1 = int(input("\nEnter the number of the file you wish to use\n"))
            # reads the file and stores it in a dataframe    
            # time start
            tic = time.perf_counter()
            self.data = pd.read_csv(filenames[user_input1])
            toc = time.perf_counter()
            # time ends
            print(f"Loaded file in {toc - tic:0.4f} seconds")
        except:
            print("An error happened when loading the file")
            self.load_data()
        
    def search_functionality(self):
        #ask user input for search
        print("Searching Value in Data")
        user_input = str(input("Enter anything to search data\n"))
        print("Filtered Value in Data Based on Search Values\n")
        if user_input.isnumeric():
            print("You've entered a number.")
            user_input_int = int(user_input)
            if self.data[self.data.eq(user_input_int).any(axis=1)].shape[0] != 0:
                print(self.data[self.data.eq(user_input_int).any(axis=1)])
        elif self.data[self.data.eq(user_input).any(axis=1)].shape[0] != 0:
            print("You've entered a string.")
            print(self.data[self.data.eq(user_input).any(axis=1)])
        else:
            print("Nothing was found.")
        
    def print_data(self):
        try:
            user_input = int(input("\nEnter the number of rows you want to print out (up to 5000):\n")) 
            if user_input > 5000:
                print("Please enter a number between 0 and 5000")
                self.print_data()   
            else:
                print(self.data.head(user_input)) 
        except:
            print("An error happened when entering your input.") 
            self.print_data()
        

    def distinct_column_values(self):
        i = 0
        list_col_name = list(self.data.columns)
        print("")
        #takes column names and prints into a user readable list
        for x in list_col_name:
                print(i, x)
                i = i + 1
        user_input = int(input("\nEnter a Column Number to show unique values \n"))
        #takes user input and displays unique column values
        try :
            unique = self.unique_function(list_col_name[user_input])
            size = len(unique)
            print("\nThere are",size,"unique values in this column.")
        except:
            print("An error happened when looking for column name. Try again.\n")
            self.describe_data()

    def explore_data (self):
        # Requirements:
        # list all columns in the dataset and offer the user the possibility of drop any of them        COMPLETED by Miguel 
        # Count distinct values of any column selected by the user                                      COMPLETED by Ed
        # Search any value in any column as input by the user                                           COMPLETED by Esmeralda
        # Sort any columns (Ascending or descending) as selected by the user                            COMPLETED by Miguel
        # Print the first 100, 1000 or 5000 rows of the dataset as selected by the user                 COMPLETED by Alex and Esmeralda
        flag = True
        while flag:
            print(" Please Select an Option.")
            print(" 21. List All Columns:")    
            print(" 22. Drop Columns:")
            print(" 23. List Column Ascending or Descending:")
            print(" 24. Count Distinct Values of Any Column:")
            print(" 25. Search Any Value In Any Column:") 
            print(" 26. Print The Number Of Rows:")
            print(" 27. Back to Main Menu")   
            print("--------------------------------------------------")
            user_input = str(input("\nEnter the number from the menu\n"))
            if user_input == '21':
                # time start
                tic = time.perf_counter()
                self.col_names()
                toc = time.perf_counter()
                # time ends
                print(f"Time measured {toc - tic:0.4f} seconds") 
                print("--------------------------------------------------")
            elif user_input == '22':
                # time start
                tic = time.perf_counter()
                self.drop_col()
                toc = time.perf_counter()
                # time ends
                print(f"Time measured {toc - tic:0.4f} seconds")
                print("--------------------------------------------------")
            elif user_input == '23':
                # time start
                tic = time.perf_counter()
                self.col_ascend_descend()
                toc = time.perf_counter()
                # time ends
                print(f"Time measured {toc - tic:0.4f} seconds")
                print("--------------------------------------------------")
            elif user_input == '24':
                # time start
                tic = time.perf_counter()
                self.distinct_column_values()
                toc = time.perf_counter()
                # time ends
                print(f"Time measured {toc - tic:0.4f} seconds")
                print("--------------------------------------------------")
            elif user_input == '25':
                # time start
                tic = time.perf_counter()
                self.search_functionality()
                toc = time.perf_counter()
                # time ends
                print(f"Time measured {toc - tic:0.4f} seconds")
                print("--------------------------------------------------")
            elif user_input == '26':
                # time start
                tic = time.perf_counter()
                self.print_data()
                toc = time.perf_counter()
                # time ends
                print(f"Time measured {toc - tic:0.4f} seconds")
                print("--------------------------------------------------")
            elif (user_input == '27'):
                flag = False
                break
            else:
                #there was an else here but was creating an error
                print("\nInvalid input. Try again.")
    
      
    def count_function(self, columnName):
        print("Count the number of rows")
        list_data = self.data[columnName].values.tolist()
        number = []
        number.append(len(list_data))          
        return number


    def max_function(self, columnName):
        x = self.data[columnName].values.tolist()
        value1 = 0
        for value2 in x:
            if (value1 <= value2):
                value1 = value2
        return value1
    
    def min_function(self, columnName):
        x = self.data[columnName].values.tolist()
        value1 = 100000000000000000000000000000000000000000000000000000
        for value2 in x:
            if (value2 <= value1):
                value1 = value2
        return value1
    
    #Get all unique values in a specified column
    def unique_function(self, column_name):
        unique_values = []
        data = self.data[column_name]
        for value in data:
            if (value not in unique_values):
                unique_values.append(value)
        return unique_values
    
    def percentile(self, column_name, perc):
        #Documentation: https://stackoverflow.com/questions/2374640/how-do-i-calculate-percentiles-with-python-numpy
        #Documentation: https://stackoverflow.com/questions/32558805/ceil-and-floor-equivalent-in-python-3-without-math-module
        data = self.data[column_name].values.tolist()
        size = len(data)
        #ceiling
        num = -( -(size * perc) // 100)
        #sorted
        return sorted(data)[int(num) - 1]
    
    def mean_func(self, column_name):
        data = self.data[column_name].values.tolist()
        size = len(data)
        sum_val = 0
        for d in data:
            sum_val += d
        return float(sum_val/size)

    def median_function(self, column_name):
        column_data = self.data[column_name].values.tolist()
        column_data.sort()
        median = 0.0
        if (len(column_data) % 2 == 0):
            median = column_data[len(column_data)//2]
        else:
            temp = column_data[len(column_data)//2]
            temp2 =  column_data[(len(column_data)//2) - 1]
            median = (temp + temp2)//2
        return median

    def mode_function(self, column_name):
        frequency = {}
        column_data = self.data[column_name].values.tolist()
        for j in column_data:
            if not j in frequency:
                frequency[j] = 1
            else:
                frequency[j] += 1
        return max(frequency, key = frequency.get)
    
    def variance_function(self, column_name):
        #Documentation: https://blog.finxter.com/how-to-get-the-variance-of-a-list-in-python/#:~:text=Python%20List%20Variance%20Without%20NumPy,variance%20in%20a%20generator%20expression.
        data = self.data[column_name].values.tolist()
        avg = sum(data) / len(data)
        var = sum((x-avg)**2 for x in data) / len(data)
        return var

    def describe_data(self):
        # Requirements:
        # Count                         COMPLETED by Esmeralda
        # Unique                        COMPLETED by Alex
        # Mean                          
        # Median                        Completed by Alex
        # Mode                          Completed by Alex
        # Standard Deviation (SD)
        # Variance
        # Minimum                       COMPLETED by Esmeralda
        # Maximum                       COMPLETED by Esmeralda
        # 20 Percentile (P20)           COMPLETED by Esmeralda
        # 40 Percentile (P40)           COMPLETED by Esmeralda
        # 50 Percentile (P50)           COMPLETED by Esmeralda
        # 60 Percentile (P60)           COMPLETED by Esmeralda
        # 80 Percentile (P80)           COMPLETED by Esmeralda
        # time start
        tic = time.perf_counter()
        i = 0
        list_col_name = list(self.data.columns)
        numbers = []
        print("")
        for ele in list_col_name:
            if self.data[ele].dtype.kind in 'iufc':
                print(i, ele)
                i = i + 1
            
        user_input = int(input("\nEnter a Column Number to show stats \n"))
        try :
            numbers = self.count_function(list_col_name[user_input])
            print("\nNumber of rows: ", numbers[0])
            #print("Number of columns: ", numbers[1])
            unique = self.unique_function(list_col_name[user_input])
            print("\nUnique values")
            print(unique)
            mean = self.mean_func(list_col_name[user_input])
            print("\nMean", mean)
            minnum = self.min_function(list_col_name[user_input])
            print("\nMinimum Value: ", minnum)
            median = self.median_function(list_col_name[user_input])
            print("\nMedian Value: ", median)
            mode = self.mode_function(list_col_name[user_input])
            print("\nMode Value: ", mode)
            variance = self.variance_function(list_col_name[user_input])
            print("\nVariance", variance)
            maxnum = self.max_function(list_col_name[user_input])
            print("\nMaximum Value: ", maxnum)
            percent = self.percentile(list_col_name[user_input], 20)
            print("\n20 Percentile: ", percent)
            percent = self.percentile(list_col_name[user_input], 40)
            print("\n40 Percentile: ", percent)    
            percent = self.percentile(list_col_name[user_input], 50)
            print("\n50 Percentile: ", percent)       
            percent = self.percentile(list_col_name[user_input], 60)
            print("\n60 Percentile: ", percent)      
            percent = self.percentile(list_col_name[user_input], 80)
            print("\n80 Percentile: ", percent)  
        except:
            print("An error happened when looking for column name. Try again.\n")
            self.describe_data()
        toc = time.perf_counter()
        # time ends
        print(f"Time measured {toc - tic:0.4f} seconds")
        
        
    def analyze_data (self):
        # Requirements:
        # How many airlines are included in the data set? Print the first 5 in alphabetical order.                                          COMPLETED by Ed
        # How many departing airports are included in the data set? Print the last 5 in alphabetical order.                                 COMPLETED by Esmeralda 
        # What airline has the oldest plane?                                                                                                COMPLETED by Miguel 
        # What was the greatest delay ever recorded? print the airline and airpots of this event.                                           COMPLETED by Alex
        # What was the smallest delay ever recorded? print the airline and airports of this event.                                          COMPLETED by Alex
        # What was the month of the year in 2019 with most delays overall? And how many delays were recorded in that month?                 COMPLETED by Esmeralda
        # What was the month of the year in 2019 with most delays overall? And how many delays were recorded in that day?                   COMPLETED by Esmeralda
        # What airline carrier experience the most delays in January, July and December                                                     COMPLETED by Alex
        # What was the average plane age of all planes with delays operated by American Airlines inc.                                       COMPLETED by Alex
        # How many planes were delayed for more than 15 minutes during days with "heavy snow" (Days when the inches of snow on ground were 15 or more) )?   COMPLETED by Ed
        # What are the 5 airports (Deaprting Airpots) that had the most delays in 2019? Print the airports and the number of delays         COMPLETED by Ed
        tic = time.perf_counter()
        self.analysis()
        toc = time.perf_counter()
        # time ends
        print(f"Time measured {toc - tic:0.4f} seconds")

        
    def analysis(self):
        #analysis 1
        print("1. How many airlines are included in the data set? Print the first 5 in alphabetical order.");
        list_num_air = self.data['CARRIER_NAME'].tolist()
        result = []
        [result.append(a) for a in list_num_air if a not in result]
        count = len(result)
        result.sort()
        print("\nThere are " , count, " Airlines in the data set.")
        print("\nFirst 5 in alphabetical order")
        for i in range(5):
            print(result[i])
        print("--------------------------------------------------")
        
        print("2. How many departing airports are included in the data set? Print the last 5 in alphabetical order.\n")
        #filter and store into list_data 
        list_dep_air = self.data['DEPARTING_AIRPORT'].tolist()
        result = []
        #remove duplicates and print out how many airports are included in the data set
        [result.append(x) for x in list_dep_air if x not in result]
        count = len(result)
        result.sort()
        print("\nThere are " , count, " departing airports in the data set.")
        result = result[-5:]
        print("\nLast 5 in alphabetical order")
        for ele in result:
            print(ele)
        print("--------------------------------------------------")
        
        # What airline has the oldest plane? Print the 5 airlines that have the 5 oldest planes recorded.
        print("\n3. What airlines have the oldest plane? \n")
        print(self.data.loc[self.data['PLANE_AGE'] > 28].pivot_table(columns=['PLANE_AGE', 'CARRIER_NAME'], aggfunc='size'))
        print("--------------------------------------------------")
        
        # Question 4
        unique_airlines= self.unique_function('CARRIER_NAME')
        unique_ports = self.unique_function('DEPARTING_AIRPORT')
        passengers_per_port = [0] * len(unique_ports)

        count = 0
        for word in unique_ports:
            filt = (self.data['DEPARTING_AIRPORT'] == word)
            avg_passengers = self.data.loc[filt, 'AVG_MONTHLY_PASS_AIRPORT'].values.tolist()
            for elements in range(len(avg_passengers)):
                passengers_per_port[count] = passengers_per_port[count] + avg_passengers[elements]                
            passengers_per_port[count] = int(passengers_per_port[count]/len(avg_passengers))
            count += 1
        
        # Store the top five averages and th name of the airport that it corresponds too
        ranks = sorted([(x,i) for (i,x) in enumerate(passengers_per_port)], reverse = True)
        top_five_avgs = []
        top_ports = []
        for x,i in ranks:
            if i&x not in top_five_avgs:
                top_five_avgs.append(x)
                top_ports.append(unique_ports[i])
                if (len(top_five_avgs) == 5):
                    break
        print("4. Top 5 airports that averaged the greatest number of passengers:")
        for i in range(5):
            print("     ",top_ports[i],", number of passengers:", top_five_avgs[i])
        print("--------------------------------------------------")

        # Analysis question 5
        count = 0
        total_worker = [0] * len(unique_airlines)
        for word in unique_airlines:
            filt = (self.data['CARRIER_NAME'] == word)
            ground_service = self.data.loc[filt, 'GROUND_SERV_PER_PASS'].values.tolist()
            flight_attendents = self.data.loc[filt, 'FLT_ATTENDANTS_PER_PASS'].values.tolist()
            for elements in range(len(ground_service)):
                total_worker[count] = total_worker[count] + ground_service[elements]
                total_worker[count] = total_worker[count] + flight_attendents[elements] 
            total_worker[count] = total_worker[count]/len(unique_airlines)
            count += 1

        dictionary = {}
        for i in range(len(total_worker)):
            dictionary[unique_airlines[i]] = total_worker[i]
        top_five = sorted(dictionary.items(), key = lambda item:item[1], reverse = True)
        count = 0
        print("5. Print the 5 airlines that averaged the greatest number of employees per passenger:")
        for key, value in sorted(dictionary.items(), key=lambda kv: kv[1], reverse=True):
            count += 1
            print("     %s: %s" % (key, value))
            if(count == 5):
                break
        print("--------------------------------------------------")
        
        print("")
        print("6. What was the month of the year in 2019 with most delays overall? And how many delays were recorded in that month?\n")
        list_mon = self.data['MONTH'].tolist()
        list_days = self.data['DAY_OF_WEEK'].tolist()
        list_dep_del = self.data['DEP_DEL15'].tolist()
        mon_final_list = [0] * 12
        merged_list = [(list_mon[i], list_days[i], list_dep_del[i]) for i in range(0, len(list_mon)) if list_dep_del[i] == 1]
        for j in range(1, 13):
            for i in range(0, len(merged_list)):    
                if merged_list[i][0] == j:
                    mon_final_list[j-1] += 1
        value1 = 0
        mon_idx=0
        for value2 in mon_final_list:
            if (value1 <= value2):
                value1 = value2
                mon_idx = mon_idx +1
        print("Month with Most Delays: ", mon_idx+1)
        print("Max Delays: ", value1)
        print("--------------------------------------------------")
        
        print("")
        print("7. What was the month of the year in 2019 with most delays overall? And how many delays were recorded in that day?\n")
        day_final_list = [0] * 12
        #print(merged_list)
        for j in range(1, 8):
            for i in range(0, len(merged_list)):
                if merged_list[i][0] == mon_idx+1:    
                    if merged_list[i][1] == j:
                        day_final_list[j-1] += 1
        value1 = 0
        day_idx=0
        for value2 in day_final_list:
            if (value1 <= value2):
                value1 = value2
                day_idx = day_idx +1
        print("Since the DAY_OF_WEEK only goes from 1 to 7, which is the number of days in a week, and does not have which week each entry corresponds to,")
        print("the following answer calculates how many delays there were for day number, 1 to 7.")
        print("Day with Most Delays in Month", mon_idx+1, "is", day_idx+1)
        print("Max Delays for that day and month:", value1)
        print(day_final_list)
        print("--------------------------------------------------")
        
        # Question 8
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
        print("--------------------------------------------------")
        
        #Analysis Question 9
        filt = (self.data['CARRIER_NAME'] == 'American Airlines Inc.') & (self.data['DEP_DEL15'] == 1)
        planeAges = self.data.loc[filt, 'PLANE_AGE'].values.tolist()
        avg_plane_age = 0;
        for i in range(len(planeAges)):
            avg_plane_age = avg_plane_age + planeAges[i]
        avg_plane_age = avg_plane_age / len(planeAges)
        print("\n9. What was the average plane age of all planes with delays operated by American Airlines inc.?")
        print("The average plane age of American Airlines inc. which had delays was:",int(avg_plane_age), "years old")
        print("--------------------------------------------------")
        
        #Analysis Question 10
        print("""\n10. How many planes were delayed for more than 15 minutes during days with "heavy snow" (Days when the inches of snow on ground were 15 or more)? """)
        list_num_delays = self.data['DEP_DEL15'].tolist()
        list_snow_days = self.data['SNWD'].tolist()
        count = 0
        merge = [ (list_num_delays[i], list_snow_days[i]) for i in range(0, len(self.data)) if list_num_delays[i] == 1]
        for j in range(0, len(merge)): 
            if list_snow_days[j] > 14.9: 
              count = count + 1  
        print ("\nThere were",count,"planes that were delayeed by heavy snow in 2019")
        print("--------------------------------------------------")
        
        #Analysis Question 11
        #What are the 5 airports (Deaprting Airpots) that had the most delays in 2019? Print the airports and the number of delays
        num_months = [1,2,3,4,5,6,7,8,9,10,11,12]
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        count = 0
        print("\n11. What are the 5 airports (Deaprting Airpots) that had the most delays in 2019?")
        for i in num_months:
            filt = (self.data['DEP_DEL15'] == 1)    
            temp = self.data.loc[filt, 'DEPARTING_AIRPORT'].values.tolist()
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
        print("--------------------------------------------------")  

    # List out all the Columns Names
    def col_names(self):
        # loops through the data and prints out the colums individualy
        i = 1
        cols = self.data.columns.tolist()
        for c in cols:
            print("Column", i, "name is:", c)
            i = i + 1


    # Drops a column from the dataset
    def drop_col(self):
        # Gives time in H:M:S format
        time = str(datetime.datetime.utcnow().strftime("%H:%M:%S"))
        # shows the amount of columns making it easier to type in for user
        self.col_names()
        try:
            colName = str(input("\n%s Enter The Column's Name You Wish To Drop (e.g. 'PREVIOUS_AIRPORT')\n" % time))
            dropCol = self.data.drop(columns=[colName])
            print(dropCol)
            return dropCol
        except:
            
            print("sorry you dong goofed up plz try again")
            self.drop_col()
        
        
        

    # Lists out all the values from column selected in either ascending or descending manner
    def col_ascend_descend(self):
        # shows the amount of columns making it easier to type in for user
        self.col_names()
        colName = str(input("\nEnter a Column name (e.g. 'PREVIOUS_AIRPORT')\n"))
        try:
            userInput = int(input("\nDo You Wish To See The Column In Ascending Order (0) Or Descending Order (1)?"))
    
            if (userInput == 1):
                print(self.data.sort_values(by=[colName], ascending=False, na_position='first'))

            
            elif (userInput == 0):
                print(self.data.sort_values(by=[colName], ascending=True, na_position='first'))

                
            else:
                print("Sorry but The Number You Inputted Was Wrong Please Try Again")
                self.col_ascend_descend()
        except:    
                #else:
            print("Sorry Something Went Wrong When Inputting The Column's Name Plz Try Again")
            self.col_ascend_descend()        
        

def main():
    input_flag = True
    print("Please note that this project will only work with the 2019 Airline Delay Dataset.")
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
        elif user_input == '2':
            d.describe_data()
        elif user_input == '3':
            d.analyze_data()
        elif user_input == '4':
            d.load_data()
        elif (user_input == 'q') or (user_input == 'Q') :
            input_flag = False
            break
        else:
            print("Invalid input. Enter a valid input.")
if __name__ == "__main__":
    main()
