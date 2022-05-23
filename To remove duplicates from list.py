ls1=list(map(int,input().split()))
for i in ls1:
    c=ls1.count(i)
    for j in range(c-1):
             ls1.remove(i)
print(ls1)
