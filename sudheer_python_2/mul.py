try:
    f=open("C://python//example2.txt","r")
    print(f.read())

except FileNotFoundError as e:
    print("not found",e)
else:
    print("ALL FINE")
