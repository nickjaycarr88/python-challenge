import os
import csv

pybank_csv = os.path.join("budget_data.csv")

with open(pybank_csv,encoding='utf-8-sig') as csv_file:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)
    months_years = []
    list = []
    ints_list = []

    for row in csv_reader:
        list.append(row[1])
        months_years.append(row[0])

    for element in list:
        ints_list.append(int(element))


# print(type(ints[3]))

new_list = []
for i in range(0,len(ints_list)-1):
    a = ints_list[i]
    b = ints_list[i+1]
    if a > 0 and b > 0:#done
        if a > b:#done
            c = (a - b) * -1
            new_list.append(c)
        else:#done
            d = b - a
            new_list.append(d)
    elif a < 0 and b > 0:#done
         e = (a* -1) + b 
         new_list.append(e)
    elif a > 0 and b < 0: 
         f = b - a
         new_list.append(f)
    elif a < 0 and b < 0:
        if a > b:
            g = (a * -1) + b
            new_list.append(g)
        else:
            h = (b * -1) + a
            new_list.append(h)
list_sum = sum(new_list)

greatest_decrease_in_profits = min(new_list)
greatest_decrease_in_profits_index = new_list.index(greatest_decrease_in_profits)

greatest_increase_in_profits = max(new_list)
greatest_increase_in_profits_index = new_list.index(greatest_increase_in_profits)

print(months_years)
print(months_years[greatest_decrease_in_profits_index + 1])
print(months_years[greatest_increase_in_profits_index + 1])
print(list_sum)
print(len(new_list))
print(min(new_list))
print(max(new_list))
print(len(new_list))
print(new_list)
print(sum(ints_list))


    




            




