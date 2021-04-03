import os
import re

paragraph = open("paragraph_1.txt", "r")

number_of_lines = 0
number_of_words = 0
number_of_characters = 0
sentance_list =[] 

for line in paragraph:
  line = line.strip("\n")
  words = line.split()

  number_of_lines += 1
  number_of_words += len(words)
  number_of_characters += len(line)
#full_stops = 0  
#for stop in lines:
#    full_stops = full_stops + len(stop.count('.'))
#print ('total stops:    ', full_stops)

re.split(r'[.!?]+', paragraph)

paragraph.close()

print("lines:", number_of_lines, "words:", number_of_words, "characters:", number_of_characters)
print(words)
print(len(words))