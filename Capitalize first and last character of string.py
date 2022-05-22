st=input()
l=st.split()
s=' '
for i in l:
    s+=i[0].upper()+i[1:len(i)-1]+i[-1].upper()+" "
print(s)
