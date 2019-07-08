n = int(input())
nus = list(map(int,input().split()))
temps = []
for i in range(n):
    if nus[i] == i:
        temps.append(nus[i])
if len(temps) == 0:
    print(-1)
else:
    for i in sorted(temps):
        print(i,end=' ')
