num=int(input())
val=[0 for n in range(0,num+1)]
print(val)
for i in range(0,num+1):
    if(i==0):
        val[i]=0
    elif(i==1):
        val[i]=1
    else:
        val[i]=val[i-1]+val[i-2]
print(val)
