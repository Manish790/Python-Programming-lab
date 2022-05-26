num=int(input())
fact=1
if num>1:
  for i in range(1,n+1):
    fact*=i
  print(fact)
elif num==0 or num==1:
  print(1)
else:
  print("Invalid Number")
  
