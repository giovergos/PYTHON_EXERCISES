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
    

        
    
