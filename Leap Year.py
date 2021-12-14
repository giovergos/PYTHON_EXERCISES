year = int(input('year = '))
disekto = False
if year%100==0:
    if year%400==0:
        disekto = True
elif year%4==0:
    disekto = True
if disekto==True:
    print('True')
else:
    print('False')
