def getNum(n):
    i = 1
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

c=getNum(100)
print(next(c))
print(next(c))
for i in range(0,20):
    print(next(c))
