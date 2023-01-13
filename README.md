# python-challenge
## PyBank
### In this Challenge, you are tasked with creating a Python script to analyse the financial records of your company. The dataset is composed of two columns: "Date" and "Profit/Losses".
Your task is to create a Python script that analyses the records to calculate each of the following values:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period

### A portion of the code to calculate the above calculations
```python
#writing to a text file saved in another folder
output_file = os.path.join("..","analysis","analysis.txt")

with open(output_file,"w") as f:
    f.write("Financial Analysis\n")
    f.write("*************************\n")
    f.write(f"\nTotal months: " + str(amount_of_months))
    f.write(f"\nTotal: " + "$" + str(total_profit_and_loss_sum),)
    f.write(f"\nAverage Change: " + "$" + str(round(sum_of_average_change,2)),)
    f.write(f"\nGreatest Increase in Profits: " + greatest_increase_in_profits_month + "   " + "($" + str(greatest_increase_in_profits) + ")")
    f.write(f"\nGreatest Decrease in Profits: " + greatest_decrease_in_profits_month + "   " + "($" + str(greatest_decrease_in_profits) + ")")
```

### PyBank financial analysis results
![Image Link]()

## PyPoll

### In this Challenge, you are tasked with helping a small, rural U.S. town modernise its vote-counting process. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote

### A portion of the code to calculate the above calculations
```python
#if statement to save the winner of the election, comparing the scores of each candidate
if (charles_casper_stockham > diana_degette) and (charles_casper_stockham > raymon_anthony_doane):
    number_one = "Charles Casper Stockham"
elif (diana_degette > charles_casper_stockham) and (diana_degette > raymon_anthony_doane):
    number_one = "Diana DeGette"
elif (raymon_anthony_doane > charles_casper_stockham) and (raymon_anthony_doane > diana_degette):
    number_one = "Raymon Anthony Doane"
```

### PyBank financial analysis results
![Image Link]()
