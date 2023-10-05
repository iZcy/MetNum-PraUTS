import os
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

def printMatrix(mtr, roundV, postfix=""):
    for i in range(len(mtr)):
        printArray(mtr[i], roundV, postfix)
        print()

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

def promptError(errMsg, loopMsg):
    os.system('cls')
    print(errMsg)
    if (loopMsg != ""):
        print(loopMsg)

def mustNumber(msg, errMsg="Invalid input! Please try again!", dataType="float", loopMsg="", accept=[]):
    value = ""
    while(True):
        value = input(msg)
        if value in accept:
            break

        try:
            if (dataType == "float"):
                value = float(value)
                break
            elif (dataType == "int" or dataType == "unsigned"):
                value = int(value)
                if (dataType == "int"):
                    break
                elif (dataType == "unsigned"):
                    if (value <= 0):
                        promptError(errMsg, loopMsg)
                    else:
                        break
            continue
        except:
            promptError(errMsg, loopMsg)

    return value