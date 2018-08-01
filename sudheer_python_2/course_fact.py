import math
courses=int(input("enter no of courses"))
if courses==0:
    print("No of courses are 0")
elif courses>0:
    print("no of course combinations the student can take are :",math.factorial(courses))
