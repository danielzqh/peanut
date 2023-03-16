from operator import itemgetter

out = []
while True:
    inp = input()
    if(inp==""):
        break
    item = inp.split(",")
    out.append(tuple(item))
    
print(sorted(out,key=itemgetter(0,1,2)))
    
