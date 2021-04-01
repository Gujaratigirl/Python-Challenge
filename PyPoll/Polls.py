# module for PC/Mac file open
import os
# Module for reading cvs files
import csv
#set empty dictionary and list
vote_tallies = {}
vote_sum = 0
vote_percent = {}

pollscsv = os.path.join('..','PYPoll', 'Resources', 'election_data.csv')
with open(pollscsv, 'r') as filehandler:
    csvreader = csv.reader(filehandler, delimiter=',')
    #moves to the first row with data
    header=next(csvreader)
    for row in csvreader:
        if row[2] not in vote_tallies:
            #cand_list.append(cand_name[2])
            vote_tallies[row[2]] = 0
            vote_percent[row[2]] = 0
        vote_tallies[row[2]] += 1
        vote_percent[row[2]] += 1
        vote_sum += 1   
    
sum_d = sum(vote_percent.values())
for candidates in vote_percent:
    vote_percent[candidates] = format(vote_percent[candidates]/sum_d*100, '.3f')

winner_votes=0.000
winner=[]

for candidates,vote in vote_tallies.items():
    if int(vote_tallies[candidates]) > winner_votes:
        winner_votes=vote_tallies[candidates]
        winner= candidates

print("                                ")
print(f"Election Results")
print("------------------------------------")
print(f"Total Votes: {vote_sum}")
print("------------------------------------")

for candidates,votes in vote_percent.items() and vote_tallies.items():
    print(f"{candidates}: {vote_percent[candidates]} % ({vote_tallies[candidates]})")
print("------------------------------------")
print(f"Winner: {winner}")
print("------------------------------------")

# Specify the file to write to
output_path = os.path.join("..", 'PYPOLL', "analysis", "analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile)
    #csvwriter.writerow([f"Financial Analysis"])

    csvwriter.writerow(["                                "])
    csvwriter.writerow([f"Election Results"])
    csvwriter.writerow(["------------------------------------"])
    csvwriter.writerow([f"Total Votes: {vote_sum}"])
    csvwriter.writerow(["------------------------------------"])

    for candidates,votes in vote_percent.items() and vote_tallies.items():
        csvwriter.writerow([f"{candidates}: {vote_percent[candidates]} % ({vote_tallies[candidates]})"])
    csvwriter.writerow(["------------------------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["------------------------------------"]) 

