import os
import csv

#start out empty lists
bank_date = []
count = 0
bank_change=[]

max_value= 0
min_value= 100000
max_month="month"
min_month="Month"
previous_profitloss=867884

#total months and total sum
#bankcsv = os.path.join('..','PYBANK', 'Resources', 'budget_data.csv')
#with open(bankcsv, 'r') as text:
#    csvreader = csv.reader(text, delimiter=',')
    #moves to the first row with data
#    header=next(csvreader)



a_file = open("paragraph_2.txt", "r+")

list_of_lists = []
for line in a_file:
  #stripped_line = line.strip()
  line_list = line.split()
  list_of_lists.append(line_list)
  count += 1

data = a_file.read()
words = data.split()

a_file.close()

print(list_of_lists)
print(len(list_of_lists))
print(count)
print(words)
print(len(words))