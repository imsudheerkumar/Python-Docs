f=open("C:\\python\\file.txt","r+")
res=f.readlines()
print(res)
y={}
i=0
for x in res:
    y=x.strip()
    i=i+1


print(y)
