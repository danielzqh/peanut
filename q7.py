inp = input()
size = inp.split(',')
X = int(size[0])
Y = int(size[1])
multilist = [[0 for col in range(Y)] for row in range(X)]

for i in range (X):
    for j in range (Y):
        multilist[i][j] = i*j

print(multilist)
