s = input('s = ')
if len(s) == 1:
    print('Μήκος = 1')
else:
    flag = 1
    i=0
    while (i<(len(s)/2) and flag == 1):
        if s[i] != s[len(s)-1-i]:
            flag = 0
        else:
            i+=1
    if flag == 0:
        print('Δεν είναι παλίνδρομο')
    else:
        adict = {s : len(s)}
        alist = [ ]
        for i in range(len(s)):
            alist.append(s[i])
        print(adict, alist, sep='\n')
    
