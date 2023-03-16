lines = []
while True:
    s = input()
    if s:
        lines.append(s)
    else:
        break

for items in lines:
    print(items.upper())
