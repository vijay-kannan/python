nn,m=map(int,input().split())
tem=[]
x=0
for ma in range(nn):
    tem.append(list(map(int,input().split())))   
for ma in range(nn):
    for j in range(m-1):
        for k in range(j+1,m+1):
            if tem[ma][j:k]==[1]*len(tem[ma][j:k]):
                 if all(tem[p+ma][j:k]==[1]*len(tem[p+ma][j:k]) for p in range(len(tem[ma][j:k])-1)):
                     if len(tem[ma][j:k])>x:
                        x=len(tem[ma][j:k])
if len(tem)==1 and len(tem[0])==1 and tem[0][0]==1:
    print(1)
for ma in range(x):
    print(*[1]*x) 
