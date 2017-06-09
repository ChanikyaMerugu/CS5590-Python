#reversing 789
a=789 #number assign
r=0
while (a!=0): #loop condition
    k=a%10 #remainder
    r=r*10+k
    a=a//10 #number using in nextloop
print(r)


