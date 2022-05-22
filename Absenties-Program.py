l1=list(map(int.input().split()))
print("Roll No of Absenties are: ",end=" ")
for i in range(1,20):
    if i not in l1:
        print(i,end=' ')
