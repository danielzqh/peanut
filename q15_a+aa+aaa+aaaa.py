a= input()
num1 = int(a)
num2 = int("%s%s" % (a,a))
num3 = int("%s%s%s" % (a,a,a))
num4 = int("%s%s%s%s" % (a,a,a,a))

print(num1+num2+num3+num4)
