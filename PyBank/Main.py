import os
import csv

# Read path
Main_file = os.path.join("..", "PyBank", "budget_data.csv")

# Define file stream
with open(Main_file) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    # Enable next row past titles
    next(csv_reader)
    revenue = []
    date = []
    change_in_revenue = []
    average_change = []

    # For loop defines date and revenue
    for row in csv_reader:
        date.append(row[0])
        revenue.append(float(row[1]))

    # For loop defines calulations
    for i in range(1, len(revenue)):
        change_in_revenue.append(revenue[i] - revenue[i-1])
        average_change = sum(change_in_revenue)/len(change_in_revenue)
        greatest_increase = max(change_in_revenue)
        greatest_decrease = min(change_in_revenue)
        increase_date = str(date[change_in_revenue.index(max(change_in_revenue))])
        decrease_date = str(date[change_in_revenue.index(min(change_in_revenue))])

    # Print results
    with open("Budget_data.txt", "w") as txt_file:
        txt_file.write("Financail Analysis\n")
        txt_file.write("-------------------------------------------------------------\n")
        txt_file.write("Total Months:" + str(len(date)) + "\n")
        txt_file.write("Total Revenue: $" + str(sum(revenue)) + "\n")
        txt_file.write("Average Change: $" + str(round(average_change, 2)) + "\n")
        txt_file.write("Greatest Increase in Profits:" + increase_date + "$" + str(round(greatest_increase, 2)) + "\n")
        txt_file.write("Greatest Decrease in Profits:" + decrease_date + "$" + str(round(greatest_decrease, 2)) + "\n")
        print("Financail Analysis")
        print("-------------------------------------------------------------")
        print("Total Months:", len(date))
        print("Total Revenue: $", sum(revenue))
        print("Average Change: $", round(average_change, 2))
        print("Greatest Increase in Profits:", increase_date, "$", round(greatest_increase,))
        print("Greatest Decrease in Profits:", decrease_date, "$", round(greatest_decrease,))
