check=int(input())
listuu=[]
for i in range(check):
    listuu.extend(list(map(int,input().split())))
print(*sorted(listuu))
