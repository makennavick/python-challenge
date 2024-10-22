
"""PyBank Homework."""

# Dependencies
import csv
import os

# Files to import & export
file_to_load = os.path.join("Resources", "budget_data.csv")  
file_to_output = os.path.join("analysis", "budget_analysis.txt")

# Define variables to track the financial data
total_months = 1        # set = 1 to include the first month since we will be skipping that row of data
total_net = 1088983     # same reasoning as above. found this number upon my initial look at the csv file

# Add more variables to track other necessary financial data
max_increase = 0        # greatest increase in profits over the entire period
max_decrease = 0        # greatest decrease in profits over the entire period
prev_month = 1088983    # previous month's profits
net_change_list = []    # we will add to this after every month
current_month_name = []

# Open and read the csv
with open(file_to_load, 'r', encoding='UTF-8') as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader) # note: this was the data we stored in total_months & total_net

    #Track the total and net change

    # Process each row of data
    for row in reader:

        # Recognize the values in the second column as integers
        new_profit = int(row[1])

        # Keep track of time
        total_months += 1 
        current_month_name.append(row[0])

        # Track the net change
        month_to_month = new_profit - prev_month    # difference in profits since the previous month
        net_change_list.append(month_to_month)      # store the month-over-month change in a list
        total_net += new_profit                     # track the overall net change
        prev_month = new_profit                     # save this as the previous month's info before we move onto the next month

    
# Calculate the greatest increase & decrease in profits
max_increase = max(net_change_list) 
max_decrease = min(net_change_list)

# Locate the month that the greatest increase & decrease occur
index_max_increase = net_change_list.index(max_increase)
index_max_decrease = net_change_list.index(max_decrease)

max_incr_month = current_month_name[index_max_increase]
max_decr_month = current_month_name[index_max_decrease]


# Calculate the average net change across the months
avg_change = (sum(net_change_list) / (total_months - 1)) 

# Generate the output summary
output = f"""
          Financial Analysis
          ----------------------------
          Total Months: {total_months}
          Total: ${total_net}
          Average Change: ${round(avg_change,2)}
          Greatest Increase in Profits: {max_incr_month} (${max_increase})
          Greatest Decrease in Profits: {max_decr_month} (${max_decrease})"""

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

# Update the user
print("""

        The above results have been saved in the analysis folder.
        
     """)