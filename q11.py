inp = input()
nums = inp.split(',')
values = []
for num in nums:
    
    intnum = int(num,2)
    if(intnum%5==0):
        values.append(num)

print(','.join(values))
