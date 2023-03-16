def binary_search(li,element):
    bot = 0
    top = len(li)-1
    ind = -1
    while(top>=bot and ind==-1):
        mid = int((top+bot)/2)
        if(li[mid]==element):
            ind = mid
        elif(li[mid]>element):
            top = mid-1
        else:
            bot = mid+1
    return ind

li = [3,4,5,6,7,8,9,10,11,12]
ele = 5
index = binary_search(li,ele)
print(index)
