n=int(input("Enter Number between 1 To 6 : "))
dc={1:2}
start=2
for i in range(n):
  d=start**2
  dc[start]=d
  start=d
print(dc)
