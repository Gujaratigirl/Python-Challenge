# module for PC/Mac file open
import os

# Module for reading cvs files
import csv
#start out empty list
bank_date = []
bank_change = 0
#bank_change_int = 0
bank_change_list1 = []
#bank_change_list2 = []
bank_change_new=[]

bankcsv = os.path.join('..', 'pybank', 'budget_data.csv')
with open(bankcsv, 'r') as text:
    csvwriter = csv.reader(text, delimiter=',')
    #moves to the first row with data
    header = next(csvwriter)

    for bank_value in csvwriter:
        bank_date.append(bank_value[0])
        #bank_change_list1.append(int(bank_value[1]))
        #adding with += function for change price
        bank_change += int(bank_value[1])
        #current_value=int(bank_value[1])
        #future_value=int(bank_value[1]+1)
        #bank_change_list2.append(int(bank_value[1]))




#print(bank_date)
#print(bank_change)

#length of bank_date
bank_date_length=len(bank_date)
print (f"Total Months: {bank_date_length}")

print(f"Total: ${bank_change}")
#print(bank_change_list1)
#bank_change_list2.pop(0)
#print(bank_change_list2)

for i in bank_change_list1:
    bank_change_new.append[bank_change_list1(i+1)]

print (bank_change_new)

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module




#with open(csvpath) as FileHandler:
   # next(FileHandler)
    # CSV reader specifies delimiter and variable that holds contents
    #csvreader = csv.reader(FileHandler, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
   # csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
   # for row in csvreader:
   #     print(row)

#make new file and write into it what is calculated
#bank_output = os.path.join("..", "pybank", "bank_output.csv")
#with open(bank_output, 'w', newline='') as csvfile:
    # Initialize csv.writer
    #csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    #csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

    # Write the second row
    #csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])

    #print(f"Expert status: {expert_status}")
