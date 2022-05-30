txt=input()
with open('appended.txt', 'a+') as f:
    f.write(txt)
    f.seek(0)
    data=f.read()
    print(data)
    
