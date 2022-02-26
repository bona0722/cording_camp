import re

ar = input()
n = len(ar)

sec = []
ans = 0
  

def arithmetic_op(num, arrN):
  global ar
  pass
  # if ar[arrN] == '-':
  #   sec.append(num)
  #   arithmetic_op(num-1, arrN+2)
  #   sec.pop()
  # elif ar[arrN] =='+':
  #   arithmetic_op(num+4, arrN+2)
  # elif ar[arrN] =='*':
  #   arithmetic_op(num*4, arrN+2)
    
    


def found_alpha():
  if ar[0] == 'a':
    a = 4
    arithmetic_op(a)
  elif ar[0] == 'b':
    b = 4
  elif ar[0] == 'c':
    c = 4
  elif ar[0] == 'd':
    d = 4
  elif ar[0] == 'e':
    e = 4 
  elif ar[0] == 'f':
    f = 4 



arithmetic_op(4, 2)
found_alpha()