def is_even(n):
    return n%2==0

li = [1,2,3,4,5,6,7,8,9,10]
#evennum = filter(is_even, li)
#evennum is a array, need to convert to list before printout
evennum = filter(lambda x: x%2==0, li)
print(list(evennum))
