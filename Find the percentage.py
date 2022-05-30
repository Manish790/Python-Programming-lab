x=int(input())
st=[]
for i in range(x):
    st+=input().split()
query=input()
ind=st.index(query)
for i in range(len(st)):
   su= float(st[ind+1])+float(st[ind+2])+float(st[ind+3])
   p=su/3
print('%.2f'%p)
