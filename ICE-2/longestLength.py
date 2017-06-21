list1 = ['hello','haaaa','haha','hoho','there','india','chanikyaaa']
max1 = ''
for x in range (0, len(list1)):
    if (len(max1) < len(list1[x])):
        max1 = list1[x]

print(max1,len(max1))




