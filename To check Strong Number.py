n=input()
sum,l=0,len(n)
for i in n:
    sum+=eval(i)**l
print("Strong Number") if eval(n)==sum else print("Not Strong Number")
