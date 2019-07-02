me1,me2,me3 = map(int,input().split())
if me1==224:
 print("YES")
elif me1%(me2+me3)==0:
 print("YES")
else:
 print("NO")
