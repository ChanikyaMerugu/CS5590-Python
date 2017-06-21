import string                                           #importing string
a=set(string.ascii_lowercase)                          #Assigning all lower case values to 'a'
str= input('enter string')                             #input from user
k=set(str)                                             #assigning all values in string from user to k

if k>=a :                                              #checking condition
  print('true')
else:
  print('false')                                      #printing output