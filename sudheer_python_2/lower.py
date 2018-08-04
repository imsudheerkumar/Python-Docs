str=input("enter string")
count=0
count2=0
for i in str:
    if(i.islower()):
        count=count+1
    elif (i.isupper()):
        count2=count2+1
print("lower case :",count)
print("upper case :",count2)

