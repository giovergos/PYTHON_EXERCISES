#A program that reads an alphanumeric and checks if it is palindromic. If it is true, the program shows a dictionary named 'adict' that includes only one pair, having the alphanumeric as the key and its length as the value. Also it shows a list named 'alist' that includes as elements the characters of the alphanumeric.
#If the alphanumeric isn't palindromic, it shows 'Δεν είναι παλίνδρομο' (means 'It is not palindromic') and stops. No need to check the input, consider that it is always capital letters and at least one character (letter or number).

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
    
