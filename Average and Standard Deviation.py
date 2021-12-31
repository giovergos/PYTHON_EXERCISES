"""
A program that reads a file named "inputdata.txt" and then:
a) calculates the average number and the standard deviation of the readen values from "inputdata.txt"
b) creates the file "outputdata.txt" and saves to it the values of the average number and the standard deviation
the inputdata file is already existed and the values of the average number and the standard deviation have to be floats with 3 decimals.
"""

from statistics import mean, stdev

with open('inputdata.txt', 'r') as f:
    content = f.read().splitlines()
numlist = []
for i in content:
    numlist.append(float(i))
avg = round(mean(numlist), 3)
stad = round(stdev(numlist), 3)

with open('outputdata.txt', 'w') as f2:
    f2.write('Μέσος όρος = ' + str(avg) + '\n')
    f2.write('Τυπική απόκλιση = ' + str(stad) + '\n')

