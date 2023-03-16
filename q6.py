C = 50
H = 30
ss = input()
list = ss.split(',')
values = []
for l in list:
    D = int(l)
    Q = (2 * C * D / H) ** (1/2)
    values.append(str(round(Q)))
    
print(','.join(values))
