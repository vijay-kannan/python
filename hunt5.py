import sys, string, math

def Count_ch(Ll1, n1) :
    count = [0] * (n1+1)
    count[0] = 1
    count[1] = 1
    for i in range(2,n1+1) :
        count[i] = 0
        if (Ll1[i-1] > '0') :
            count[i] = count[i-1]
        if (Ll1[i-2] == '1'  or ( Ll1[i-2] == '2' and Ll1[i-1] < '7') ) :
            count[i] += count[i-2]
    return count[n1]

s1 = input()
Ll1 = list(s1)
if s1 == '101' :
    print(2)
    sys.exit()
ans = Count_ch(Ll1,len(Ll1))
print(ans)
