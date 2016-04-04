names= ['mike', 'bob', 'joel', 'hannah', 'cooper', 'cool', 'hip']
offday_list=[]
week= 'N, S'
week= raw_input('Is it an N or S week?')
if week== 'N':
    for i in range(8):
        names.pop(i-1 and i-2)
        offday_list.append(i-1 and i-2)
if week== 'S':
    for i in range(11):
        names.pop(i-1 and i-2)
        offday_list.append(i-1 and i-2)
print week
