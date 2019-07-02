vv1,vkk=input().split()
sr=0
if len(vv1)>len(vkk):
  vv1,vkk=vkk,vv1
p=0
while q<len(vv1):
  sr+=(ord(vkk[q])-ord(vv1[q]))
  q+=1
for q in range(q,len(vkk)):
  sr+=ord(vkk[q])-ord('a')+1
print(sr)
© 2019 GitHub, Inc.
