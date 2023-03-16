def evenGenerator(n):
    i=0
    while i<=n:
        if(i%2==0):
            yield i
        i+=1

num=int(input())
val=[]

##for i in range(0,num+1):
##    if(i%2==0):
##        val.append(str(i))
for i in evenGenerator(num):
    val.append(str(i))

print(",".join(val))
