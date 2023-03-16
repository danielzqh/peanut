import random

print(random.random()*90+10)

print(random.random()*90+5)

li=[i for i in range(11) if i%2==0]
print(random.choice(li))

li2=[i for i in range(201) if i%5==0 and i%7==0]
print(random.choice(li2))

li3=[i for i in range(100,201)]
print(random.sample(li3,5))

li4=[i for i in range(100,201) if i%2==0]
print(random.sample(li4,5))

li5=[i for i in range(1,1001) if i%5==0 and i%7==0]
print(random.sample(li5,5))

li6=[i for i in range(7,16)]
print(random.choice(li6))
