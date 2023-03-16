dic = {}
s = input()
for c in s:
    dic[c] = dic.get(c,0)+1
print("\n".join(["%s,%s" % (k, v) for k, v in dic.items()]))
