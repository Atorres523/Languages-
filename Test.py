import csv
import os
from os import listdir
from itertools import islice
import pprint
# Define a class to hold an individual row of data from the CSV file.
# each row will correspond to its own object

# global variable
def find_csv_filenames(path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith(suffix) ]

class Row:
    def __init__(self, column):
        self.month = column[0]                      # Month
        self.day = column[1]                        # Day of Week
        self.depart_delay = column[2]               # TARGET Binary of a departure delay over 15 minutes (1 is yes)
        self.depart_time = column[3]                # departure time
        self.distance_group = column[4]             # Distance group to be flown by departing aircraft
        self.seg_num = column[5]                    # The segment that this tail number is on for the day
        self.concur_flights = column[6]             # Concurrent flights leaving from the airport in the same departure block
        self.num_seats = column[7]                  # Number of seats on the aircraft
        self.carrier_name = column[8]               # Carrier
        self.airport_flights = column[9]            # Avg Airport Flights per Month
        self.airline_flights = column[10]           # Avg Airline Flights per Month
        self.airline_airport_flights = column[11]   # Avg Flights per month for Airline AND Airport
        self.avg_monthly_pass_airport = column[12]  # Avg Passengers for the departing airport for the month
        self.avg_monthly_pass_airline = column[13]  # Avg Passengers for airline for month
        self.flight_attend = column[14]             # Flight attendants per passenger for airline
        self.ground_serv = column[15]               # Ground service employees (service desk) per passenger for airline
        self.plane_age = column[16]                 # Age of departing aircraft
        self.depart_airport = column[17]            # Departing Airport
        self.lat = column[18]                       # Latitude of departing airport
        self.long = column[19]                      # Longitude of departing airport
        self.prev_airport = column[20]              # Previous airport that aircraft departed from
        self.prcp = column[21]                      # Inches of precipitation for day
        self.snow = column[22]                      # Inches of snowfall for day
        self.snwd = column[23]                      # Inches of snow on ground for day
        self.tmax = column[24]                      # Max temperature for day
        self.awnd = column[25]                      # Max wind speed for day
        self.carrier_hist = column[26]              # 
        self.depart_airport_hist = column[27]       # 
        self.day_hist = column[28]                  # 
        self.depart_block_hist = column[29]         # 
    
# Define a class to hold data from the CSV file.
class Data:
    def __init__(self):
        # this list holds all the Row objects created
        # Row[0] contains an object. That object contains the value in every 
        #  column of that row
        self.rows = []

    # Load data from a CSV file.
    def load_data(self):    
        count = 0
        dir_path = str(os.getcwd() + "/")
        filenames = find_csv_filenames(dir_path)
        print("Here are a list of the CSV Files found:\n")
        for name in filenames:
                print("%s: %s" % (str(count), name))
                count += 1
        user_input = int(input("\nEnter the number of the file you wish to use\n"))
        with open(filenames[user_input]) as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header row.
            for row in reader:
                self.rows.append(Row(row))

    # Function to retrieve the total amount of delays experience by all carriers 
    def total_delays(self):
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
            count = count + 1

# Calling functions so we can output data
#____________________________________________________

# Load the data.
d = Data()
d.load_data()

# Print the data.
print("Part 4 the analaysis questions")
d.Alex_analysis()
# d.print_data()