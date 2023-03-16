
def factor(x):
    if x==1:
        return 1
    return x * factor(x-1)

x=int(input())
print(factor(x))
