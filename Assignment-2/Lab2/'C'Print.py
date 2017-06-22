
#printing the first letter of the name using *

for r in range(7):                                          #range for number of rows
  for k in range(5):                                        #range for no of columns
    if ((k==0) or (r==0)or (r==6) and (k>0)):               #condition for printing
      print('*',end='')                                     #print * and gaps accordingly
    else:
      print(end='')
  print()                                                   #print star accordingly