import random
def generate(p, d) :
    N = len(p)
    isoccupied = [0] * N
    isselected = [0] * N
    newp = [0] * N
    altered  = list()
    dremain = d
    while(dremain > 0) :
        while(True) :
            index = random.randrange(0, N)
            if (isselected[p[index]] == 0) and (p[index] < N - 1):
                break
        isselected[p[index]] = 1
        ceiling = 0
        if increment < N - p[index] - 1 :
            ceiling = increment
        else :
            ceiling = N - p[index] - 1
        increment = random.randrange(1, ceiling + 1)
        dremain -= increment
        newp[index] = p[index] + increment
        isoccupied[newp[index]] = 1
        

    
    





generate([0, 1, 2, 3], 1)
