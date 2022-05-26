num=int(input())
s=0
for i in range(1,num):
  if num%i==0:
    s+=i
if num==s:
  print("Perfect Number")
else:
  print("Not Perfect Number")
 
