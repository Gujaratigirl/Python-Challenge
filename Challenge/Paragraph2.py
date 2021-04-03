import os
import re

paragraph = open("paragraph_1.txt", "r")

number_of_lines = 0
number_of_words = 0
number_of_characters = 0
sentance_list =[] 
number_of_sentances = 0

for line in paragraph:
  line = line.strip("\n")
  words = line.split()

  number_of_lines += 1
  number_of_words += len(words)
  number_of_characters += len(line)
  number_of_sentances = line.count('.') # can't get it to count when on multiple lines.


#full_stops = 0  
#for stop in lines:
#    full_stops = full_stops + len(stop.count('.'))
#print ('total stops:    ', full_stops)

#re.split(r'[.!?]+', paragraph)

paragraph.close()

print(len(words))
print("                                ")
print(f"Paragraph Analysis")
print("------------------------------------")
print(f"Approximate Word Count: {number_of_words}")
print(f"Approximate Sentance Count: {number_of_sentances}")
print(f"Average Letter Count: {format(number_of_characters/number_of_words, '.2f')}") #  this is to drive number of decimil places
print(f"Average Sentance Length: {number_of_words /number_of_sentances} ")
print("                                ")
