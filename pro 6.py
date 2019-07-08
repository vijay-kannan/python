X=int(input())
Y=list(map(int,input().split()))
b1=0
for x in range(len(Y)-2):
    for y in range(x+1,len(Y)-1):
        for z in range(y+1,len(Y)):
            if Y[x]<Y[y]<Y[z] and x<y<z:
                b1=b1+1
print(b1)
