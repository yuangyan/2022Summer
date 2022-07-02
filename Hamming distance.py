import random
def HammingDistance(a, b) :
    d = 0
    if len(a) != len(b) :
        d = -1
        return d

    N = len(a)
    for i in range(N) :
        if a[i] != b[i] :
            d += 1
    return d
    
def DeriveDistance1(a: list, d) : 
    N = len(a)
    isselected = [0] * N
    dremain = d

    index2change = list()
    indexvalues = list()
    while (dremain > 0) :
        index = random.randrange(0, N)
        if isselected[index] == 0 :
            dremain -= 1
            index2change.append(index)
            indexvalues.append(a[index])
    
    isavalable = [1] * d

    notsuccess = True
    while(notsuccess) :
        for i in range(d) :
            while(True) :
                newindex = random.randrange(0, d)
                if()
        

        


      