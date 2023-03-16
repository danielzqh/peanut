li=[12,24,35,24,88,120,155,88,120,155]
newli = []
set1 = set()

for item in li:
    if item not in set1:
        set1.add(item)
        newli.append(item)

print(set1)
print(newli)

