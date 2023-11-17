import os
import csv

output_path= os.path.join("Resources","budget_data.csv")

def financial_analysis(Resources,budget_data):
    # Initialize variables
    total_months = 0
    net_total = 0
    prev_profit_loss = 0
    profit_losses_changes = []
    months = []
total_months = 0
net_total = 0
prev_profit_loss = 0
profit_losses_changes = []
months = []

with open(output_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)  # Skip header row
        
        for row in csvreader:
            # Extract data from the row
            date = row[0]
            profit_loss = int(row[1])

            # Calculate total number of months
            total_months += 1

            # Calculate net total amount of profit/losses
            net_total += profit_loss

            # Calculate changes in profit/losses and store them
            if total_months > 1:
                change = profit_loss - prev_profit_loss
                profit_losses_changes.append(change)
                months.append(date)

            # Update previous profit/loss for the next iteration
            prev_profit_loss = profit_loss

 # Calculate average change in profit/losses
average_change = sum(profit_losses_changes) / len(profit_losses_changes)

    # Find greatest increase and decrease in profits
greatest_increase = max(profit_losses_changes)
greatest_decrease = min(profit_losses_changes)

    # Find corresponding months for greatest increase and decrease
increase_month = months[profit_losses_changes.index(greatest_increase)]
decrease_month = months[profit_losses_changes.index(greatest_decrease)]

    # Display results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")