amount = int(input("Enter the Amount: "))
tth=amount//2000
amount -=2000*tth
fh=amount//500
amount-=500*fh
th=amount//200
amount-=200*th
h=amount//100
amount-=100*h
print(f'''Number of 2000 notes are {tth}
Number of 500 notes are {fh} 
Number of 200 notes are {th} 
Number of 100 notes are {h}''')
