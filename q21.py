xval = 0
yval = 0
while True:
    inp = input()
    if(inp=="" or inp=="!"):
        break
    items = inp.split(" ")
    if(items[0]=="UP"):
        yval+=int(items[1])
    if(items[0]=="DOWN"):
        yval-=int(items[1])
    if(items[0]=="LEFT"):
        xval+=int(items[1])
    if(items[0]=="RIGHT"):
        xval-=int(items[1])

#print(xval*xval+yval*yval)    
dist = (xval*xval+yval*yval) ** (1/2)
print(round(dist))
    
