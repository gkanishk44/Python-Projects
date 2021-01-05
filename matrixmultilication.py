X = [[9,4,9],
    [5,5,5],
    [2,4,8]]

Y = [[54,38,11,29],
    [61,71,37,8],
    [41,57,49,6]]

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

for i in range(len(X)): 
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
