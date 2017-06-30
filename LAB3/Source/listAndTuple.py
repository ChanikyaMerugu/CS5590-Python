# program to convert to list and tuple.

wrd = input("Word Please!!")                      #  input from user

if (wrd != ""):                                   #checking codition
    lstWrd = []
    tpleWrd = ()


    for str in wrd:                               #for loop condition
        lstWrd.append(str)
        tpleWrd += (str,)                         #appendig the string
    print(lstWrd)
    print(tpleWrd)                                #printing the tple and wrd
else:
    print("word.")