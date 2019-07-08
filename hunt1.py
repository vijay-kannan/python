nu=int(input())
lil=list(map(int,input().split()[:nu]))
#d=len(lil)
c=[]
for i in range(len(lil)):
    l=i+1
    for j in range(l,len(lil)):
        if (lil[i]==lil[j] and lil[i] not in c):
            c.append(lil[i])
c.sort()
print(*c,end=' ')
if len(c)==0:
    print("unique")
