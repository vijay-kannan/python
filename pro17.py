numm=input()
a=list(map(int,numm.split()))
k=a[1]
h=input()
flag=0
sv=list(map(int,h.split()))
for i in range(0,len(sv)-1):
	for j in range(i+1,len(sv)):
		if sv[i]+sv[j]==k:
			print("yes")
			flag=1
			break
	if flag==1:
		break
if flag!=1:
	print("no")
