print("Enter the string:")
H=input()
def frequency(H):
    dict = {}
    for i in H:
        keys = dict.keys()
        if i in keys:
            dict[i] = dict[i]+ 1
        else:
            dict[i] = 1
    return dict
print(frequency(H))