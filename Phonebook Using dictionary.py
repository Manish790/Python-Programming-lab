n=int(input())
d=dict(input().split() for x in range(n))
ls=[]
for j in range(n):
    x=input()
    ls.append(x)

for i in ls:
    if i in d:
       print(f"{i}={d[i]}")
    else:
        print("Not found")
