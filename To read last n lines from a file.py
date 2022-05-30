n=int(input("lines: "))
with open('data.txt', 'r') as f:
    for i in range(n):
        data=f.readlines()[-n:]
        print(*data,sep='\n')
