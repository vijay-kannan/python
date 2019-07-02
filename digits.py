from itertools import combinations
s,v2=input().split()
v2=int(v2)
l=[]
dd=combinations(s,len(s)-v2)
for i in list(dd):
  l.append("".join(i))
print(min(l))
