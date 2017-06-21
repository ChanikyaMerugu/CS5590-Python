
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
print('\n avg of numbers is', sum/count)