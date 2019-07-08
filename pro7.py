    
#harika
b=[]
n=int(input())
for i in range(0,n-1):
    b.append(abs(n-(2**i)))
print(min(b))
