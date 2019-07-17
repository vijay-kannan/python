def count_1(n) :
    ss = bin(n)[2:]
    k = ss.count('1')
    return k
n = int(input())
L = [ int(x) for x in input().split()]
Ls2 = []
for i in range(0,n) :
    Ls2.append((count_1(L[i]),L[i]))
L3 = sorted(Ls2, key=lambda x : (x[0],x[1]),reverse=True)
L4 = [x[1] for x in L3 ]
for i in range(0,len(L4)) :
    print(L4[i])
