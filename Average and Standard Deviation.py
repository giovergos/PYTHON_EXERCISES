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

