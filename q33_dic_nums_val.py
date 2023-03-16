def dic_nums():
    dnum = {}
    for i in range(1,21):
        dnum[i] = i**2
    for (k,v) in dnum.items():
        print(v)

dic_nums()
