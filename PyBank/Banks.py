# module for PC/Mac file open and readig csv files
import os
import csv

#start out empty lists
bank_date = []
bank_sum = 0
bank_change=[]

max_value= 0
min_value= 100000
max_month="month"
min_month="Month"
previous_profitloss=867884

#total months and total sum
bankcsv = os.path.join('..','PYBANK', 'Resources', 'budget_data.csv')
with open(bankcsv, 'r') as text:
    csvreader = csv.reader(text, delimiter=',')
    #moves to the first row with data
    header=next(csvreader)
    # first_row = next(csvreader)-- couldn't get this to work so just used first value.

    for bank_value in csvreader:
        bank_date.append(bank_value[0])
        current_profitloss=int(bank_value[1])

        #adding with += function for change price
        bank_sum += int(bank_value[1])
        bank_value.append(current_profitloss-previous_profitloss)
        previous_profitloss=current_profitloss
        #print(bank_value)
        bank_change.append(bank_value[2])

        if int(bank_value[2])> max_value:
            max_value= int(bank_value[2])
            max_month=bank_value[0]
        if int(bank_value[2])< min_value:
            min_value= int(bank_value[2])
            min_month= bank_value[0]

#From class activity
def average(list):
    length=len(list)
    total =0.0
    for number in list:
        total +=number
    return total /length

#length of bank_date
bank_date_length=len(bank_date)
#remove head '0' from list
bank_change.pop(0)

#average_change = (format(average(bank_change), '.2f')
average_percent = f"{format(average(bank_change), '.2f')}"

#Print out results
print("                                ")
print(f"Financial Analysis")
print("------------------------------------")
print(f"Total Months: {bank_date_length}")
print(f"Total: ${bank_sum}")
print(f"Average Change: ${format(average(bank_change), '.2f')}" )#  this is to drive number of decimil places
print(f"Greatest Increase in Profits: {max_month} (${max_value})" )
print(f"Greatest Decrease in Profits: {min_month} (${min_value})" )
print("                                ")


# Specify the file to write to
output_path = os.path.join("..", 'PYBANK', "analysis", "analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile) ## 'delimiter=',''what does this really do???

    csvwriter.writerow([f"Financial Analysis"])
    csvwriter.writerow(["------------------------------------"])
    csvwriter.writerow([f"Total Months: {bank_date_length}"])
    csvwriter.writerow([f"Total: ${bank_sum}"])
    csvwriter.writerow([f"Average Change: ${average_percent}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {max_month} (${max_value})" ])
    csvwriter.writerow([f"Greatest Decrease in Profits: {min_month} (${min_value})" ])