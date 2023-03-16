import re
inp = input()
'''
items = inp.split(" ")
nums = []
for item in items:
    if re.match("\d+", item):
        nums.append(item)
print(nums)
                
'''
print(re.findall("\d+",inp))
