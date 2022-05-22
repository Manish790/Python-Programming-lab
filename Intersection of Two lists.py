ls1=list(map(int,input().split()))
ls2=list(map(int,input().split()))
for i in ls2:
    if i in ls1:
        print(i,end=" ")
