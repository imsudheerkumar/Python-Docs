def modify(string):  
  final = ""   
  for i in range(len(string)):  
    if i % 2 == 0:  
      final = final + string[i]  
  return final
string=input("Enter string:")
res=modify(string)
print("modified string is :",res)
print("reverse of modified string :",res[::-1])
