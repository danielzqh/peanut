total = 0
while True:
    inp = input()
    if(inp==""):
        break
    values = inp.split(" ")
    if(values[0]=="D"):
        total+=int(values[1])
    if(values[0]=="W"):
        total-=int(values[1])
    else:
        pass
print(total)
    
