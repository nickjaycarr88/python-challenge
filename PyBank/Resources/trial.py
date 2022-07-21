import os
import csv

pybank_csv = os.path.join("budget_data.csv")

with open(pybank_csv,encoding='utf-8-sig') as csv_file:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)
    #a list to store the months/years from the csv file
    months_years = []
    #this list holds the data of profit/ loss from the csv file
    profit_loss_list = []
    #this list changes the data from profit_loss_list from string to integer
    ints_list = []
    #pushing data from csv file to above created lists
    for row in csv_reader:
        profit_loss_list.append(row[1])
        months_years.append(row[0])
    #changing the profit and loss data from str to int
    for element in profit_loss_list:
        ints_list.append(int(element))
#this new_list_avg saves the difference between one month and the next
new_list_avg = []
#iterating through the data and pushing the difference from profit and loss 
for i in range(0,len(ints_list)-1):
    a = ints_list[i]
    b = ints_list[i+1]
    c = b-a
    new_list_avg.append(c)
    #the total profit and loss sum for the period
    total_profit_and_loss_sum = sum(ints_list)
    #the amount of months recorded
    amount_of_months = len(months_years)
    #the average change is the sum of all the diffrence in profit and loss for the period, divided by the amount of difference from month to month
    sum_of_average_change = sum(new_list_avg)/(len(new_list_avg))
    #recoding the greatest increase from month to month for the period
    greatest_increase_in_profits = max(new_list_avg)
    #using the above greatest increse, finding which index it is in the list
    greatest_increase_in_profits_index = new_list_avg.index(greatest_increase_in_profits)
    #using the index number from above calculation and finding which matching month/year it is in the months_years list
    greatest_increase_in_profits_month = months_years[greatest_increase_in_profits_index + 1]
    #recoding the greatest decrease from month to month for the period
    greatest_decrease_in_profits = min(new_list_avg)
    #using the above greatest increse, finding which index it is in the list
    greatest_decrease_in_profits_index = new_list_avg.index(greatest_decrease_in_profits)
    #using the index number from above calculation and finding which matching month/year it is in the months_years list
    greatest_decrease_in_profits_month = months_years[greatest_decrease_in_profits_index + 1]

print("Financial Analysis")
print("*"*25)
print(f"Total months: " + str(amount_of_months))
print(f"Total: " + "$" + str(total_profit_and_loss_sum))
print(f"Average Change: " + "$" + str(round(sum_of_average_change,2)))
print(f"Greatest Increase in Profits: " + greatest_increase_in_profits_month + "   " + "($" + str(greatest_increase_in_profits) + ")")
print(f"Greatest Decrease in Profits: " + greatest_decrease_in_profits_month + "   " + "($" + str(greatest_decrease_in_profits) + ")")

