# -*- coding: UTF-8 -*-
"""PyBank Homework."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
max_increase = 0    # greatest increase in profits over the /entire/ period - incl date and amount
max_decrease = 0    # greatest decrease in profits over the /entire/ period - incl date and amount
prev_month = 0   # previous month's profits
net_change_list = [] # we will add to this after every month

# Open and read the csv
with open(file_to_load, 'r', encoding='UTF-8') as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    # ???? we did that above. doing this would mean we're getting rid of the first row of data?? first_row = next(reader) # this row: ['Jan-10', '1088983']

    # Track the total and net change

    # Process each row of data
    for row in reader:

        # Recognize the second column values as integers
        new_profit = int(row[1])

        # Track the total number of months
        total_months += 1 

        # Track the net change
        month_to_month = new_profit - prev_month # difference in profits since the previous month
        net_change_list.append(month_to_month) # store the month-over-month change in a list
        total_net += new_profit # track the overall net change
        prev_month = new_profit # save this as the previous month's info before we move onto the next month

        # Calculate the greatest increase in profits (month and amount)
        max_increase = max(net_change_list) # these need to be OUT of the for loop

        # Calculate the greatest decrease in losses (month and amount)
        max_decrease = min(net_change_list)
# print(f'Biggest month:{max_increase}, lowest month:{max_decrease}, overall net:{total_net}')


# Calculate the average net change across the months
avg_change = mean(net_change_list)

# Generate the output summary


# Print the output


# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
