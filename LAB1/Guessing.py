
import random                              #importing random library
rand = random.randint(0,9)                 #generating random number
print(rand)
NoG=0
while NoG==0 :                             #loop creation
    a = int(input('guess a number'))
    if rand == a:                          #check condition
        print ('you guessed it right')
        NoG=1
    elif rand > a:                          #check condition
         print('guess a bit higher digit')
    elif rand < a:                          #check condition
        print('guess a bit lower digit')

print('end')









