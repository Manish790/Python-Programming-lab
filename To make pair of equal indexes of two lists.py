x1=list(map(int,input().split()))
x2=list(map(int,input().split()))
x=[(x1[i],x2[j]) for i in range(len(x1)) for j in range(len(x2)) if i==j]
print(x)
