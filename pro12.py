b,r=map(int,input().split())
last=list(map(int,input().split()))
l=[]
for i in range(0,r):
     x,y=map(int,input().split())
     l.append([x,y])
for i in range(r):
     lower=lin[i][0]
     upper=l[i][1]
     m=sum(last[lower-1:upper])
     print(m)
