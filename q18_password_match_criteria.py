import re

def match(pas):
    if(not re.search("[a-z]",pas)):
        return False
    if(not re.search("[0-9]",pas)):
        return False
    if(not re.search("[A-Z]",pas)):
        return False
    if(not re.search("[$#@]",pas)):
        return False
    if(len(pas)<6 or len(pas)>12):
        return False
    return True


inp = input()
passwords = inp.split(",")
out = []
for pas in passwords:
    if(match(pas)):
        out.append(pas)
print(",".join(out))

