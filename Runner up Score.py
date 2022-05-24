lst=list(eval(input()))
m=max(lst)
for i in range(lst.count(m)):
    lst.remove(m)
print(max(lst))


