<<<<<<< HEAD
UI = input("Enter a word to calculate num of digits and alphabets:")
alpha = 0
num = 0
i = 0
l = len(UI)
while i < len(UI):
    if UI[i].isalpha():
        alpha = alpha + 1
    elif UI[i].isnumeric():
        num = num + 1
    i = i + 1
=======
UI = input("Enter a word to calculate num of digits and alphabets:")
alpha = 0
num = 0
i = 0
l = len(UI)
while i < len(UI):
    if UI[i].isalpha():
        alpha = alpha + 1
    elif UI[i].isnumeric():
        num = num + 1
    i = i + 1
>>>>>>> 6c926a1c43c3b530d8567d9d7892aaee56d27cc6
print("digits ", num ,"alphabets", alpha)