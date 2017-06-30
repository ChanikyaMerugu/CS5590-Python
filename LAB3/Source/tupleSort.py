#  Program to sort tuple in increasing order
import operator
N_list = [(7, 6), (5, 7), (4, 3), (1, 2), (1, 8)]


def execute(lst):                                           #execute function
    if isinstance(lst,list):
        return True
    else:
        return False                                       #returning false if condition fails

if(execute(N_list)):
    print(sorted(N_list,key=lambda y:(y[1],-y[0])))                     #Lambda function
    N_list.sort(key=operator.itemgetter(1))
    print(N_list)


else:                                                                  #ccondition false
    print("Error")


