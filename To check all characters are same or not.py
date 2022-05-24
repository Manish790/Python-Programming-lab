st=input()
re=False
for i in range(len(st)-1):
    x=st[0]
    if(x==st[i+1]):
        re=True
print("All characters are same") if re==1 else print("None")
