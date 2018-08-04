str=input("enter string")
count=0
count2=0
for i in str:
    if(i.isdigit()):
        count=count+1
    elif (i.isalnum()):
        count2=count2+1
print("digits :",count)
print("letters :",count2)

