#A function-generator that receives unlimited integer numbers and returns consecutively the square of the subtraction's result of every value with the all value's average.
#To check the function, make a program that calls it, having as parameters the numbers 3,4,5. No need to check if the user gives integer numbers. Use the statistics library and the command 'return'.

import statistics

def squares(*args):
    if args==0:
        return 0
    else:
        mo=statistics.mean(args)
        for i in args:
            yield pow(i-mo, 2)
            
for i in squares(3,4,5):
    print(i, end=' ')
