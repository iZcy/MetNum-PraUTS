from sympy import *

# Creating Methods
x = symbols('x')

# Evaluate X-Input
def evToX(f, val):
    return N(f.subs(x, val))

# Array Printer
def printArray(arr, roundV, postfix=""):
    print("[", end="")
    for i in range(len(arr)):
        if (i != 0):
            print(", ", end="")
        print(str(round(arr[i], roundV))+postfix, end="")
    print("]", end="")

# Array to Function
def arrToFunc(vect):
    stringify = ""
    for i in range(len(vect)):
        # Extract values
        coef = str(vect[i])
        powr = "x**" + str(i)
        stringed = ""

        # Combine per operator
        if not (i == 0):
            if not (coef[0] == "-"):
                stringed += " +"
            else:
                stringed += " "

        # Combine per operand
        stringed += (coef + "*" + powr)

        # Export
        stringify += stringed

    # Print Test
    # print("String function:", stringify)
    funct = sympify(stringify)

    return funct