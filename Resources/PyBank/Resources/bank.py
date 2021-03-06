# * In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# * Your task is to create a Python script that analyzes the records to calculate each of the following:

#   * The total number of months included in the dataset

#   * The net total amount of "Profit/Losses" over the entire period

#   * The average of the changes in "Profit/Losses" over the entire period

#   * The greatest increase in profits (date and amount) over the entire period

#   * The greatest decrease in losses (date and amount) over the entire period

import os
import csv 


#Open the csv file and set delimiter to ',' 
budget_data = os.path.join("budget_data.csv")
with open(budget_data, 'r') as csvfile:
    next(csvfile)
    csvreader = csv.reader(csvfile, delimiter = ',')
#set a variable equal to the total number of months of data within the csv
    total_months = sum(1 for row in csvreader)
    print(total_months)

#define a function that will analyze any budget_data in the same format as the csv.
def analysis(budget_data):
    total_months = 0 
    net_profit = 0
    current_month = 0 
#set a variable lastmonth = None, use this to track current_change in logic statement 
    lastmonth = None
    current_change = 0 
    change = []
    max_rev = 0 
    min_rev = 0 
    for row in budget_data:
        month = row[0]
        total_months += 1 
        current_month = int(row[1])
        net_profit = net_profit + current_month
# track current_change in profit using the value stored in current_month and lastmonth
        if lastmonth is not None: 
            current_change = current_month - lastmonth
            change.append(current_change)
# write logic statements that will update the months with max revenue and mininmum revenue based on current change. 
            if current_change > max_rev:
                max_rev = current_change
                maxmonth = month
            if current_change < min_rev:
                min_rev = current_change
                minmonth = month
        lastmonth = current_month
    average_change = sum(change)/len(change)

    return [total_months, net_profit, max_rev, min_rev, maxmonth, minmonth, average_change]

# generate output summary by running function on the csv file
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvfile)
    analyzed = analysis(csvreader)
output_summary = print(
    f"""Total months: {analyzed[0]}\n
    net profit: {analyzed[1]}\n
    max revenue: {analyzed[2]}, {analyzed[4]}\n
    min revenue: {analyzed[3]}, {analyzed[5]}\n
    average change: {analyzed[6]}
""")

# delcare output_path which will hold a text file with the analysis of the financials for that fiscal year. 
output_path = os.path.join("..", "output", "financials.txt")

if not os.path.isdir("../output"):
    os.mkdir("../output")
else:
    pass

with open(output_path, "a") as f:
    print(
    f"""Total months: {analyzed[0]}\n
    net profit: {analyzed[1]}\n
    max revenue: {analyzed[2]}, {analyzed[4]}\n
    min revenue: {analyzed[3]}, {analyzed[5]}\n
    average change: {analyzed[6]}
""", file = f)

