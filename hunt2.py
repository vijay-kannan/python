nu=int(input())
l1=list(map(int,input().split()))[:nu]
rev=0
l1.sort(reverse=True)
for i in l1:
  rev=rev*10+i
print(rev)
