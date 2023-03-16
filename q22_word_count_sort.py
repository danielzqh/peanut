inp = input()
items = inp.split(" ")
dcount = {}
for word in items:
    dcount[word] = dcount.get(word,0) + 1

words = list(dcount.keys())
words.sort()

for k in words:
    print("%s:%d" % (k,dcount[k]))
