<<<<<<< HEAD
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
=======
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
>>>>>>> 6c926a1c43c3b530d8567d9d7892aaee56d27cc6
print(frequency(H))