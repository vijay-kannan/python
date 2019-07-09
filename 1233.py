a=input()
s=input()
s=s.split()
for d in s:
    if s.count(d)==1:
        print(d)
        break
