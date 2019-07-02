vv1,vkk=input().split()
sr=0
if len(vv1)>len(vkk):
  vv1,vkk=vkk,vv1
p=0
while p<len(vv1):
  sr+=(ord(vkk[p])-ord(vv1[p]))
  p+=1
for p in range(p,len(vkk)):
  sr+=ord(vkk[p])-ord('a')+1
print(sr)
© 2019 GitHub, Inc.
