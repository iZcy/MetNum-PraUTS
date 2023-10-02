from sympy import *

funct = "2*x"

try:
  funct = sympify(funct)
except:
  print("Invalid Function Input!")
  exit()