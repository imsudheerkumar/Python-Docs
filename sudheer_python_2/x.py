x=[[1,1,1],
   [1,1,1],
   [1,1,1]]

y=[[1,1,1],
   [1,1,1],
   [1,1,1]]

z=[[0,0,0],
   [0,0,0],
   [0,0,0]]

for i in range(len(x[0])):
    for j in range(len(x[0])):
       z[i][j] = x[i][j] + y[i][j]

for r in z:
   print(r)
