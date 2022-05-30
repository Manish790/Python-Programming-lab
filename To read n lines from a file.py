n=int(input("Enter Number of Lines To Read: "))
with open('data.txt') as f:
    for i in range(n):
        data=f.readline()
        print(data)
