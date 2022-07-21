import os
import csv

pypoll_csv = os.path.join("election_data.csv")

with open(pypoll_csv,encoding='utf-8-sig') as csv_file:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)
    #emmpty list to store the candidates names in after read from a csv file
    candidates = []
    
    # gathering the information in row 2 from csv file and pushing it to empty "candidates" list
    for row in csv_reader:
        candidates.append(row[2])
       
        #setting variables and counting the amount of times each candidate appears in the "candidates" list    
        charles_casper_stockham = candidates.count("Charles Casper Stockham")
        diana_degette = candidates.count("Diana DeGette")
        raymon_anthony_doane = candidates.count("Raymon Anthony Doane")
        #a variable to save the length of the candidates list
        total_votes = len(candidates)

    
#if statement to save the winner of the election, comparing the scores of each candidate
if (charles_casper_stockham > diana_degette) and (charles_casper_stockham > raymon_anthony_doane):
    number_one = "Charles Casper Stockham"
elif (diana_degette > charles_casper_stockham) and (diana_degette > raymon_anthony_doane):
    number_one = "Diana DeGette"
elif (raymon_anthony_doane > charles_casper_stockham) and (raymon_anthony_doane > diana_degette):
    number_one = "Raymon Anthony Doane"



print("Election Results")
print("-"*25)   
print(f"Total Votes: " + str(total_votes) )
print("-"*25)
print(f"Charles Casper Stockham: " + str(round((charles_casper_stockham/total_votes)*100,3)) + "%    " + "(" + str(charles_casper_stockham) + ")")
print(f"Diana DeGette: " + str(round((diana_degette/total_votes)*100,3)) + "%    " + "(" + str(diana_degette) + ")") 
print(f"Raymon Anthony Doane: " + str(round((raymon_anthony_doane/total_votes)*100,3)) + "%    " + "(" + str(raymon_anthony_doane) + ")")
print("-"*25)
print(f"Winner:   " +str(number_one))
print("-"*25)

output_file = os.path.join("..","analysis","analysis.txt")

with open(output_file,"w") as f:
    f.write("\nElection Results")
    f.write("\n*************************")  
    f.write(f"\nTotal Votes: " + str(total_votes) )
    f.write("\n*************************")
    f.write(f"\nCharles Casper Stockham: " + str(round((charles_casper_stockham/total_votes)*100,3)) + "%    " + "(" + str(charles_casper_stockham) + ")")
    f.write(f"\nDiana DeGette: " + str(round((diana_degette/total_votes)*100,3)) + "%    " + "(" + str(diana_degette) + ")") 
    f.write(f"\nRaymon Anthony Doane: " + str(round((raymon_anthony_doane/total_votes)*100,3)) + "%    " + "(" + str(raymon_anthony_doane) + ")")
    f.write("\n*************************")
    f.write(f"\nWinner:   " +str(number_one))
    f.write("\n*************************")
    f.close()
