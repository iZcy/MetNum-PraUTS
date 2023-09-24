from sympy import *

# Creating Methods
x = symbols('x')

def evToX(f, val):
    return N(f.subs(x, val))

def NewtonRaphson(f, f_dif, val, roundV, errRound, limit=1000, it=0):

    # Newton Raphson Formula + Error Evaluation
    value = val - evToX(f, val) / evToX(f_dif, val)
    error = (value - val)/value

    # Updating Process
    iter = it + 1
    terminate = false

    # Simulation Terminator: Found --- 0 Error a.k.a value is found
    if (error == 0):
        print("Stopped by the exact value found")
        terminate = true

    # Terminator
    if terminate:
        print("Newton Raphson Stopped! Last Value:", value)
        return [val, it]

    return NewtonRaphson(f, f_dif, value, roundV, errRound, limit, iter, error)
  
inputVal = 0.7
inputRound = 50
errRound = 5
inputTolerance = 1e-50
func = x**10-1
func_dif = diff(x**10-1, x)

# Calling Methods
newtRaph = NewtonRaphson(f=(func), f_dif=(func_dif), val=(inputVal), roundV=(inputRound), errRound=(errRound), tolerance=(inputTolerance))