def solve(numhead, numleg):
    ns = "no solution"
    for i in range(numhead+1):
        j = numhead - i
        if i*2 + j*4 == numleg:
            return i,j
    return ns,ns

numhead=35
numleg=94
solution = solve(35,94)
print(solution)
