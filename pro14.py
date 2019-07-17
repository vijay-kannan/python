x,y=map(int,input().split())
n=list(map(int,input().split()))
m=[]
for x in range(y):
       j=list(map(int,input().split()))
       m.append(j)
for i in m:
    vj=0
    for k in range(i[0]-1,i[1]):
        vj=vj^n[k]
    print(vj) 
