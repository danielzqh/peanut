def divisible57(n):
    i=0
    while i<=n:
        if(i%5==0 and i%7==0):
            yield i
        i+=1

num=int(input())
val=[]
for i in divisible57(num):
    val.append(str(i))

print(",".join(val))
