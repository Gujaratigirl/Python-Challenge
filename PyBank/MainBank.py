# module for PC/Mac file open
import os

# Module for reading cvs files
import csv
#start out empty list
bank_date = []
bank_change = 0
bank_change_list1 = []
bank_change_list2 = []
bank_change_new=[]
previous_bank_value=0

#loop thorough a list?  HOw can I do this??
max_value=0
min_value=0

bankcsv = os.path.join('..', 'Resources', 'budget_data.csv')
with open(bankcsv, 'r') as text:
    csvreader = csv.reader(text, delimiter=',')
    #moves to the first row with data
    header = next(csvreader)

    firstrow=next(csvreader)
    bankprofitloss=int(firstrow[1])
    previous_bank_value=bankprofitloss


    for bank_value in csvreader:
        bank_date.append(bank_value[0])
        bank_change_list1.append(int(bank_value[1]))
        bank_change_list2.append(int(bank_value[1]))
        
        netprofitloss=int(bankvalue[1])-previous_bank_value
        previous_bank_value=int(bankvalue[1])

        #adding with += function for change price
        bank_change += int(bank_value[1])
  #      if bank_value[1]> max_value:  #TypeError: '>' not supported between instances of 'str' and 'int'
  #          max_value= bank_value[1]
  #      if bank_value[1]< min_value
  #          min_value= bank_value[1]


   
bank_change_list2.pop(0)
#print(bank_date)
print(bank_change)

#length of bank_date
bank_date_length=len(bank_date)
print(f"Total Months: {bank_date_length}")

print(f"Total: ${bank_change}")

def average(list):
    length=len(list)
    total =0.0
    for number in list:
        total +=number
    return total /length

print (bank_change_list1)
print (bank_change_list2)
print (bank_change_new)
#didn't work-this isn't the average should be around 446309.047
print (average(bank_change_list1))
# Didn't work- I only want 2 decimal place  HOW can I reduce it to only 2
print(float(average(bank_change_list1)))

#print max and min of list --Doesn't work
print(max(bank_change_list1))
print(min(bank_change_list1))

#loop thorough a list?  HOw can I do this??
max_value=0
min_value=100000

for bank_value in csvreader:  #ValueError: I/O operation on closed file.
        if bank_value[1]> max_value:
            max_value= bank_value[1]
            max_month=bank_value[0]
        if bank_value[1]< min_value:
            min_value= bank_value[1]
            min_month= bank_value[0]
        
print(max_value)
print(min_value)


######make new file and write into it what is calculated#### is this written correctly???
bank_output = os.path.join("..", "pybank", "bank_output.csv")
with open(bank_output, 'w', newline='') as csvfile:
    #Initialize csv.writer
   
   print(f{Financial Analysis})
   print("------------------------------------")
   print(f"Total Months: {bank_date_length}")
   print(f"Total: ${bank_change}")
   print(f"Average Change: ${average(bank_change_list1).3f}%" )#  this is to drive number of decimil places
  
### None of this is working######
    for find_max_row in csvreader:
        if max_value = max_value_row[1]
            print(f"Greatest Increase: {max_value_row[0]} (${max_value})" )


    # Write the first row (column headers)
    #csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

    # Write the second row
    #csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])

    #print(f"Expert status: {expert_status}")




