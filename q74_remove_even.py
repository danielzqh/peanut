li = [5,6,77,45,22,12,24]
li2 = [x for x in li if x%2!=0]
print(li2)

li3 = [12,24,35,70,88,120,155]
li4 = [x for x in li3 if x%5!=0 or x%7!=0]
print(li4)

li5 = [12,24,35,70,88,120,155]
li6 = [x for (i,x) in enumerate(li5) if i%2!=0]
print(li6)

li7 = [12,24,35,70,88,120,155]
li8 = [x for (i,x) in enumerate(li7) if i not in (0,4,5)]
print(li8)

li9 = [12,24,35,70,88,120,155]
li10 = [x for x in li9 if x!=24]
print(li10)
