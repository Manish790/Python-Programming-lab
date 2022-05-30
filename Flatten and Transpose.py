import numpy as np
n,m=map(int,input().split())
lst=[]
for i in range(n):
  ls=list(map(int,input().split()))
  lst.append(ls)
print(f'''{np.array(lst).T}
{np.array(lst).flatten()}''')
  

