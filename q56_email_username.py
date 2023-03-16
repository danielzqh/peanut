#inp = input()
#items = inp.split("@")
#print(items[0])

import re
email = input()
pat2 = "(\w+)@((\w+\.)+(com))"
r2 = re.match(pat2, email)
print (r2)
print (r2.group(1))
print (r2.group(2))
