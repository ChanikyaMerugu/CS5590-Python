def print_horiz_line():
    print (' --- '*k)

def print_vert_line():
    print (' |  '*(k+1))

def print_Value(value):
    print("| "+value, flush=True)

k=int(input('enter the board size'))
for i in range(k):
    print_horiz_line()
    print_vert_line ()
print_horiz_line()

valueCheck=True
l, m = k, k;
list_values = [[0 for x in range(l)] for y in range(m)]

while(True):
    user_input=input("enter board entry in (x,y) format:")
    Xvalue=int(user_input.split(",")[0])
    Yvalue=int(user_input.split(",")[0])

    if(valueCheck):
        list_values[Xvalue][Yvalue]="X"
        valueCheck = False
    else:
        list_values[Xvalue][Yvalue] = "O"
        valueCheck = True

    for rows in list_values:

        print_horiz_line()
        colCount = 0
        for element in rows:
            if(element!=0):
                print_Value(element)
    print_horiz_line()