from sympy import *

funct = "2*x**2 - 5*x  + 1"

try:
  funct = sympify(funct)
except:
  print("Invalid Function Input!")
  exit()