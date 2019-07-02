vv1,xx=input().split()
sk=abs(len(vv1)-len(xx))
for i in range(len(vv1)):
    if len(xx)==1 and xx[i] in vv1:
        break
    if vv1[i]!=xx[i]:
        sk+=1
print(sk)
