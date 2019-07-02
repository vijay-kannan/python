z1=int(input())
e1=[]
for i in range(0,z1):
    inpu=input()
    e1.append(inpu)
ci=[]
for i in zip(*e1):
    if(i.count(i[0])==len(i)):
        ci.append(i[0])
            
    else:
        break
print(''.join(ci))
