st=input()
chk=''
for i in st:
    if i  not in chk:
        print(i,"came",st.count(i),"Times")
        chk+=i
