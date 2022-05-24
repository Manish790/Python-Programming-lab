st=input()
s=''
pos=int(input())
n=int(input())
print(*(st[pos:]+st[:pos]).replace(" ","")*n)
