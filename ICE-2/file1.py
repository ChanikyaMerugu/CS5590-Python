<<<<<<< HEAD

filename=input("what file are the numbers in?")
infile=open(filename,'r')
sum = 0.0
count=0
line=infile.readline()
while line != "":
    for num in line.split(","):
        sum=sum+eval(num)
        count=count+1
    line=infile.readline()
=======

filename=input("what file are the numbers in?")
infile=open(filename,'r')
sum = 0.0
count=0
line=infile.readline()
while line != "":
    for num in line.split(","):
        sum=sum+eval(num)
        count=count+1
    line=infile.readline()
>>>>>>> 6c926a1c43c3b530d8567d9d7892aaee56d27cc6
print('\n avg of numbers is', sum/count)