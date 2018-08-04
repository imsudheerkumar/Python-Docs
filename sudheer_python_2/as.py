str1=input("enter string")
str2=input("enter string")

count1=0
count2=0

for i in str1:
    count1=count1+1
for j in str2:
    count2=count2+1
if count1>count2:
    print('count1')
else:
    print('count2')
