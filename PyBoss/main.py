# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 09:09:43 2017

@author: Cynthia
"""

import csv
import datetime
import glob
import os

# US states

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}



# Number of files starting with "paragaph" in directory
numFiles = len(glob.glob1("raw_data/", "employee_data*"))

# Create new directory to store output
os.mkdir("new_data")

# File path

for i in range(1,numFiles + 1):
    path = "raw_data/employee_data" + str(i) + ".csv"
    # Open original file
    
    file = open(path, "r")
    employ = csv.reader(file, delimiter = ',')
    
    # Create blank CSV with headers
    newFileName = "new_data/employ" + str(i) + "_new.csv"
    employ_new = open(newFileName, "w", newline = '')
    employ_new = csv.writer(employ_new, delimiter = ',')
    employ_new.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    
    # Skip headers in original file
    
    next(employ, None)
    
    # Change data
    
    for row in employ:
        first = row[1].split(" ")[0]
        last = row[1].split(" ")[1]
        dob = datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%Y')
        ssn = "***-**-" + str(row[3][7:])
        state = us_state_abbrev[row[4]]
        newrow = [row[0], first, last, dob, ssn, state]
        
    #    write new data to new csv
    
        employ_new.writerow(newrow)