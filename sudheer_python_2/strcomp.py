str1=input("enter string 1 :")
str2=input("enter string 2 :")
count1=""
count2=""
for i in str1:
    if(i.isupper()):
        count1=count1+i
for j in str2:
    if(j.isupper()):
        count2=count2+j
print(count1+count2)

