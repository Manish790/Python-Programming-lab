import numpy as np
m,n=map(int,input().split())
ls1=list()
for i in range(m):
  x=list(map(int,input().split()))
  ls1.append(x)
print(max(np.min(np.array(ls1),axis=1)))

