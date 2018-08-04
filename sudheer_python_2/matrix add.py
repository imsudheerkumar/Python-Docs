x=[[1,5,1],
   [1,15,1],
   [1,10,1]]

y=[[1,10,1],
   [1,10,1],
   [1,10,1]]

z=[[0,0,0],
   [0,0,0],
   [0,0,0]]

for i in range(len(x)):
    for j in range(len(y)):
       z[i][j] = x[i][j] * y[i][j]

for r in z:
   print(r)
