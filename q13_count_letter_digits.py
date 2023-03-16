s = input()
dic = {'LETTERS':0, 'DIGITS':0}
for c in s:
    if c.isdigit():
        dic["DIGITS"] += 1
    if c.isalpha():
        dic["LETTERS"] += 1
    else:
        pass

print("LETTERS ",dic["LETTERS"])
print("DIGITS ",dic["DIGITS"])
