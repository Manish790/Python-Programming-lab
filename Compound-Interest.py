principle= int(input("Enter Principle Amount : "))
rate= int(input("Enter Rate Percentage  : "))
time= int(input("Enter Time in Years : "))
ci= principle*(1+(rate/100))**time
amount =principle+ci
print(f" Compound Interest is {ci} and Total Amount is {amount}")
