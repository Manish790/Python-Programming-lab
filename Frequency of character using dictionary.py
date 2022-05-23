st=input()
dc={}
x=[]
for i in st:
    if i not in x:
        dc[i]=st.count(i)
        x.append(i)
print(dc)   
