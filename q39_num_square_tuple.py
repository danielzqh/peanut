def square():
    values = []
    for i in range(1,21):
        values.append(i ** 2)
    tups = tuple(values)
    print(tups)

square()
