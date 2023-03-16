inp = input()
val = []
nums = inp.split(",")
for num in nums:
    a = int(num)
    if(a%2==1):
        val.append(num)

print(",".join(val))
