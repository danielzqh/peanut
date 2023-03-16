li = [1,2,3,4,5,6,7,8,9,10]
squareevennum = map(lambda x: x ** 2, filter(lambda x: x%2==0, li))
print(list(squareevennum))
