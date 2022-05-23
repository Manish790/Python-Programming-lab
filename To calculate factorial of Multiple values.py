lst=list(map(int,input().split()))
fact=1
for i in lst:
     for j in range(1,i+1):
         fact*=j
     print(fact,end=" ")
     fact=1
     
