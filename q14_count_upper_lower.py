s = input()
dic = {"UPPER CASE":0,"LOWER CASE":0}
for c in s:
    if c.isupper():
        dic["UPPER CASE"]+=1
    if c.islower():
        dic["LOWER CASE"]+=1
    else:
        pass

print("UPPER CASE",dic["UPPER CASE"])
print("LOWER CASE",dic["LOWER CASE"])
