# Importing Packages
import copy
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

# NewtonRaphson
def NewtonRaphson(f, f_dif, val, roundV, errRound, tolerance=0.00001, limit=1000, it=0, errPrev=0):
    # Intializing Process
    if (it == 0):
        print("Start to evaluate Newton Raphson")

    # Simulation Terminator: Limit of Loop
    if (it == limit):
        print("Iteration Limit! The function is either divergent or requires more iteration!")
        return [val, it]

    # Newton Raphson Formula + Error Evaluation
    value = val - evToX(f, val) / evToX(f_dif, val)
    error = (value - val)/value

    print("Iterate: ", it+1, "\tPrevious: ", val,
          "\tCurrent: ", value, "\tError: ", round(error*100, errRound), "%")

    # Updating Process
    iter = it + 1
    terminate = false

    # Simulation Terminator: Found --- 0 Error a.k.a value is found
    if (error == 0):
        print("Stopped by the exact value found")
        terminate = true

    # Simulation Terminator: Error Tolerance --- Error difference is too small to continue
    elif (it != 0 and abs(error - errPrev) < tolerance):
        print("Stoped by the error tolerance limit")
        terminate = true

    # Simulation Terminator: Almost exact --- Change of value is too small to continue
    elif (round(val, roundV) == round(value, roundV)):
        print("Stopped by the tolerated round value")
        terminate = true

    # Terminator
    if terminate:
        print("Newton Raphson Stopped! Last Value:", value)
        return [val, it]

    return NewtonRaphson(f, f_dif, value, roundV, errRound,
                  tolerance, limit, iter, error)

# Secant Method
def SecantMethod(f, valCurr, valBef, roundV, errRound, tolerance=0.00001, limit=1000, it=0, errPrev=0):
    # Intializing Process
    if (it == 0):
        print("Start to evaluate Secant Method")

    # Simulation Terminator: Limit of Loop
    if (it == limit):
        print("Iteration Limit! The function is either divergent or requires more iteration!")
        return [round(valCurr, roundV), it]

    # Secant Method Formula + Error Evaluation
    valUpd = valCurr - (
        evToX(f, valCurr) * (
            valBef - valCurr
        )
    ) / (
        evToX(f, valBef) - evToX(f, valCurr)
    )
    error = (valUpd - valCurr)/valUpd

    print("Iterate: ", it+1, "\tPrevious: ", valCurr,
          "\tCurrent: ", valUpd, "\tError: ", round(error*100, errRound), "%")

    # Updating Process
    iter = it + 1
    terminate = false

    # Simulation Terminator: Found --- 0 Error a.k.a value is found
    if (error == 0):
        print("Stopped by the exact value found")
        terminate = true

    # Simulation Terminator: Error Tolerance --- Error difference is too small to continue
    elif (it != 0 and abs(error - errPrev) < tolerance):
        print("Stoped by the error tolerance limit")
        terminate = true

    # Simulation Terminator: Almost exact --- Change of value is too small to continue
    elif (round(valCurr, roundV) == round(valUpd, roundV)):
        print("Stopped by the tolerated round value")
        terminate = true

    # Terminator
    if terminate:
        print("Secant Method Stopped! Last Value:", valUpd)
        return [round(valUpd, roundV), it]

    return SecantMethod(f, valUpd, valCurr, roundV, errRound,
                 tolerance, limit, iter, error)


# Gauss-Seidel
def GaussSeidel(roundV, errTol, totalTerm, b_val, matrix, x_val):
    iteration = 0
    arrOut = []
    # Loop the Gauss-Seidel
    for k in range(100):
        # Copy for Error Review
        errX = copy.deepcopy(x_val)
        print("Loop :", k+1, "\nBefore: ", end="")

        # Current value Display
        printArray(x_val, roundV)

        print()

        # Single Gauss-Seidel Process
        for j in range(len(matrix)):
            val = 0
            # Adding value to the b-value
            # print("Add", b[j])
            val += b_val[j]

            for i in range(len(matrix[j])-1):
                index = (j + 1 + i) % len(matrix[j])
                # Subtracting the value to x vars with response to the DYNAMIC x-input
                # print(-vars[j][index], "x" + str(index+1))
                val -= matrix[j][index] * x_val[index]

            # Dividing the value to the analyzed x-output
            # print("Div by", vars[j][j])
            val /= matrix[j][j]

            # Move value to the storage
            x_val[j] = val

        # Error Calculation
        triggerTerminate = false

        # Error Tolerance Count
        toleratedError = 0
        zeroError = 0

        print("Current: ", end="")

        # Current value Display
        printArray(x_val, roundV)
        print()

        for i in range(len(errX)):
            errX[i] = abs((x_val[i] - errX[i])/x_val[i]) * 100

            # Terminate if the minimum error achieved
            if ((errX[i] < errTol)):
                toleratedError += 1
                if ((not triggerTerminate) and (toleratedError == totalTerm)):
                    print("Terminated by tolerated error value")
                    triggerTerminate = true

            if (errX[i] == 0):
                zeroError += 1
                if ((not triggerTerminate) and (zeroError == totalTerm)):
                    print("Terminated by zero error achieved")
                    triggerTerminate = true

        print("Error: ", end="")
        printArray(errX, roundV, postfix="%")
        print("\n")

        # Stop if there exist tolerable error
        if (triggerTerminate):
            # Save the Result
            iteration = k+1
            arrOut    = x_val
            break

    print("Result: ", end="")
    printArray(x_val, roundV)
    print()

    return [arrOut, iteration]




# Setting Up Values (for root finding)
inputBefVal = 0

inputVal = 0.7
inputRound = 50
errRound = 5
inputTolerance = 1e-50
func = x**10-1
func_dif = diff(x**10-1, x)

# Calling Methods
# newtRaph = NewtonRaphson(f=(func), f_dif=(func_dif), val=(inputVal), roundV=(inputRound), errRound=(errRound), tolerance=(inputTolerance))
# print("\n")
# secnMthd = SecantMethod(valCurr=(inputVal), valBef=(inputBefVal), roundV=(inputRound), errRound=(errRound), tolerance=(inputTolerance), f=(func), limit=(1000))

# Setting Up Values (for root formulation finding)
b = [7.85, -19.3, 71.4]
guess = [0, 0, 0]
matr = [
    [3, 10, 0.2],
    [0.1, 7, -0.3],
    [0.3, -0.2, 10]
]

# Calling Methods
gaussSeid = GaussSeidel(roundV=(4), errTol=(0.000000001), totalTerm=(3), b_val=(b), x_val=(guess), matrix=(matr))

# Making Up Conclusions:
print()
print("[Evaluation finished with the result]")
# print(f"Newton Raphson resulted in {newtRaph[0]} with {newtRaph[1]} iterations.")
# print(f"Secant Method  resulted in {secnMthd[0]} with {secnMthd[1]} iterations.")
print(f"Gauss  Seidel  resulted in the vector of:\n{gaussSeid[0]}\nin {gaussSeid[1]} iterations.")
print("[Evaluation completed]")