# module for PC/Mac file open and CSV read/write files
import os
import csv
#set empty dictionary and list
original = 0
updated = ""
vote_percent = {}

employeecsv = os.path.join('..','Python-Challenge','Challenge' ,'employee_data_short2.csv')
with open(employeecsv, 'r') as filehandler:
    csvreader = csv.reader(filehandler, delimiter=',')
    #moves to the first row with data
    header=next(csvreader)
    for employee in csvreader:
        original += 1
     #   updated = employee(1).replace(" ", ",")
     #   employee(1) = updated

    print(original)


