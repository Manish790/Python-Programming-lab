n=int(input())
l=len(bin(n))-2
for i in range(n+1):
  i=bin(i)[2:]
  p=len(i)
  if p==5:
      print("  "*(5-p)+i)
  else:
      print(" "*(l-p)+i)
  
  
