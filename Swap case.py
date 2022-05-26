def swap_case(s):
  st=''
  for i in s:
    if i.isupper():
      st+=i.lower()
    else:
      st+=i.upper()
  return st

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
