nn1,m1=list(map(int,input().split()))
l=list(map(int,input().split()))
l.sort(reverse=True)
c=0
for i in l:
  if m1==0:
    break
  q1=m1//i
  c+=q1
  m1=m1-i*(q1)
print(c)
