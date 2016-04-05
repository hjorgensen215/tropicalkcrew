names= ['mike', 'bob', 'joel']
print names
offday_list=[]
print offday_list
week= 'N, S'
week= raw_input('Is it an N or S week?')
if week== 'N':
    for i in range(4):
        myvar= names.pop(1)
        offday_list.append(myvar)
elif week== 'S':
    for i in range(4):
        myvars= names.pop(1)
        offday_list.append(myvars)
##print week
##print offday_list
##print names
