import os
import glob
import csv

# Create directory for analyzed files

os.mkdir("financial_analyses")

# How many files are there to analyze
numFiles = len(glob.glob1("raw_data/", "budget_data*"))

for i in range(1, (numFiles+1)):
        
    months = 0
    totalRev = 0
    monthRev = 0
    totalChange = 0
    
    revenue = []
    
    path = "raw_data/budget_data_" + str(i) + ".csv"
    
    # Open original file
    file = open(path, "r")
    budg = csv.reader(file, delimiter = ',')
    
    # Skip header
    next(budg, None)
    
    # Create blank text file to store analyses
    newFileName = "financial_analyses/budget_analysis_" + str(i) + ".txt"
    budg_new = open(newFileName, "w")
    
    summary = open("financial_analyses/summary.txt", "a")


    for index, row in enumerate(budg):
        
        # Count months
        months = months + 1
        
        # Total revenue
        totalRev += int(row[1])
        
        # Change in revenue between months
        changeRev = int(row[1]) - monthRev
        monthRev = int(row[1])
        if index == 0:
            changeRev = 0
        totalChange += changeRev
        avgChange = round(totalChange/months,2)
        
        # Add revenue to list
        revenue.append(int(row[1]))
    
        # Greatest decrease
        if int(row[1]) == min(revenue):
            minMonth = row[0]
            minRev = int(row[1])
        
        #Greatest increase
        if int(row[1]) == max(revenue):
            maxMonth = row[0]
            maxRev = int(row[1])
            
    # Print results
    
    print("Financial Analysis")
    print("----------------------------------")
    print("Total Months: " + str(months))
    print("Total Revenue: " + str(totalRev))
    print("Average Revenue Change: " + str(avgChange))
    print("Greatest Increase in Revenue: " + maxMonth + " ($" + str(maxRev) + ")")
    if minRev < 0:
        print("Greatest Decrease in Revenue: " + minMonth + " (-$" + str(abs(minRev)) + ")\n\n")
    else:
        print("Greatest Decrease in Revenue: " + minMonth + " ($" + str(minRev) + ")\n\n")
        
    # Print results to text file for each budget csv
    
    budg_new.write("Financial Analysis - " + "budget_analysis_" + str(i))
    budg_new.write("\n----------------------------------")
    budg_new.write("\nTotal Months: " + str(months))
    budg_new.write("\nTotal Revenue: " + str(totalRev))
    budg_new.write("\nAverage Revenue Change: " + str(avgChange))
    budg_new.write("\nGreatest Increase in Revenue: " + maxMonth + " ($" + str(maxRev) + ")")
    if minRev < 0:
        budg_new.write("\nGreatest Decrease in Revenue: " + minMonth + " (-$" + str(abs(minRev)) + ")\n")
    else:
        budg_new.write("\nGreatest Decrease in Revenue: " + minMonth + " ($" + str(minRev) + ")\n\n")
        
    budg_new.close()
    
    
    # Print results to summary file of all budget csvs
    
    summary.write("Financial Analysis - " + "budget_analysis_" + str(i))
    summary.write("\n----------------------------------")
    summary.write("\nTotal Months: " + str(months))
    summary.write("\nTotal Revenue: " + str(totalRev))
    summary.write("\nAverage Revenue Change: " + str(avgChange))
    summary.write("\nGreatest Increase in Revenue: " + maxMonth + " ($" + str(maxRev) + ")")
    if minRev < 0:
        summary.write("\nGreatest Decrease in Revenue: " + minMonth + " (-$" + str(abs(minRev)) + ")\n\n")
    else:
        summary.write("\nGreatest Decrease in Revenue: " + minMonth + " ($" + str(minRev) + ")\n\n")
        
    summary.close()