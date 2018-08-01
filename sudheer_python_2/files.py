f=open("C://python//example.txt","r")
f2=open("C://python//example2.txt","w")
for line in f:
    tokens=line.split(' ')
    res=f2.write("word count : "+ str(len(tokens))+ line)


f.close()
f2.close()

    
