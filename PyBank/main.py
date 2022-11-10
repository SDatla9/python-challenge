import csv

# Declare file location
input_file = "/Users/sandhyaranidatla/Desktop/NU-VIRT-DATA-PT-10-2022-U-LOLC/repositories/python-challenge/PyBank/Resources/budget_data.csv"

# create empty lists to iterate through specific rows for the following variables
total_months = []
total_profit = []
monthly_profit_change = []

# Open csv file in default read mode with context manager
with open(input_file, newline="", encoding="utf-8") as budget:

    # Store the contents of budget_data.csv in a variable
    reader = csv.reader(budget, delimiter=",")
    # Skip the header labels
    header = next(reader)
    # Iterate through rows in the stored file contents
    for row in reader:
        # Append the total months and total profit to their corresponding lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    # Iterate through the profits in order to get the monthly change in profits
    for i in range(len(total_profit)-1):

        # Take the difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        # Obtain the max and min of the monthly profit change list
        max_increase_value = max(monthly_profit_change)
        max_decrease_value = min(monthly_profit_change)
        # correlate max and min to the proper month using month list and index from max and min
        # +1 indicates the month associated with change or next month
        max_increase_month = monthly_profit_change.index(max_increase_value) + 1
        max_decrease_month = monthly_profit_change.index(max_decrease_value) + 1

# Print statements
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: ${round(sum(monthly_profit_change) / len(monthly_profit_change), 2)}")
print(f"Greatest increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Output files
output_file = "/Users/sandhyaranidatla/Desktop/NU-VIRT-DATA-PT-10-2022-U-LOLC/repositories/python-challenge/PyBank/analysis/output.txt"

with open(output_file, "w") as file:

    # Write methods to print to Financial_Analysis_Summary
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write(f"Total Months: {len(total_months)}\n")

    file.write(f"Total : ${sum(total_profit)}\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change) / len(monthly_profit_change), 2)}\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})\n") 
