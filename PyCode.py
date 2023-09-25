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

# NewtonRaphson


def NewtonRaphson(f, f_dif, val, roundV, errRound, tolerance=0.00001, limit=1000, it=0, errPrev=0, view=True):
    # Intializing Process
    if (it == 0):
        print("Start to evaluate Newton Raphson")

    # Simulation Terminator: Limit of Loop
    if (it == limit):
        print(
            "Iteration Limit! The function is either divergent or requires more iteration!")
        return [val, it]

    # Newton Raphson Formula + Error Evaluation
    value = val - evToX(f, val) / evToX(f_dif, val)
    error = (value - val)/value

    if view:
        print("Iterate: ", it+1, "\tPrevious: ", val, "\tCurrent: ",
              value, "\tError: ", round(error*100, errRound), "%")

    # Updating Process
    iter = it + 1
    terminate = False

    # Simulation Terminator: Found --- 0 Error a.k.a value is found
    if (error == 0):
        print("Stopped by the exact value found")
        terminate = True

    # Simulation Terminator: Error Tolerance --- Error difference is too small to continue
    elif (it != 0 and abs(error - errPrev) < tolerance):
        print("Stoped by the error tolerance limit")
        terminate = True

    # Simulation Terminator: Almost exact --- Change of value is too small to continue
    elif (round(val, roundV) == round(value, roundV)):
        print("Stopped by the tolerated round value")
        terminate = True

    # Terminator
    if terminate:
        print("Newton Raphson Stopped! Last Value:", value)
        return [val, it]

    return NewtonRaphson(f, f_dif, value, roundV, errRound,
                         tolerance, limit, iter, error, view)

# Secant Method


def SecantMethod(f, valCurr, valBef, roundV, errRound, tolerance=0.00001, limit=1000, it=0, errPrev=0, view=True):
    # Intializing Process
    if (it == 0):
        print("Start to evaluate Secant Method")

    # Simulation Terminator: Limit of Loop
    if (it == limit):
        print(
            "Iteration Limit! The function is either divergent or requires more iteration!")
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

    if view:
        print("Iterate: ", it+1, "\tPrevious: ", valCurr, "\tCurrent: ",
              valUpd, "\tError: ", round(error*100, errRound), "%")

    # Updating Process
    iter = it + 1
    terminate = False

    # Simulation Terminator: Found --- 0 Error a.k.a value is found
    if (error == 0):
        print("Stopped by the exact value found")
        terminate = True

    # Simulation Terminator: Error Tolerance --- Error difference is too small to continue
    elif (it != 0 and abs(error - errPrev) < tolerance):
        print("Stoped by the error tolerance limit")
        terminate = True

    # Simulation Terminator: Almost exact --- Change of value is too small to continue
    elif (round(valCurr, roundV) == round(valUpd, roundV)):
        print("Stopped by the tolerated round value")
        terminate = True

    # Terminator
    if terminate:
        print("Secant Method Stopped!  Last Value:", valUpd)
        return [round(valUpd, roundV), it]

    return SecantMethod(f, valUpd, valCurr, roundV, errRound,
                        tolerance, limit, iter, error, view)


# Gauss-Seidel
def GaussSeidel(roundV, errTol, totalTerm, b_val, matrix, x_val, limit=100, view=True):
    # Init Message
    print("Start to Evaluate Gauss Seidel Method")

    # Init Values
    iteration = 0
    arrOut = []
    errEnd = []
    # Loop the Gauss-Seidel
    for k in range(limit):
        # Terminate Message
        termMsg = ""

        # Copy for Error Review
        errX = copy.deepcopy(x_val)

        if view:
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
        triggerTerminate = False

        # Error Tolerance Count
        toleratedError = 0
        zeroError = 0

        if view:
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
                    termMsg = "Terminated by tolerated error value"
                    triggerTerminate = True

            if (errX[i] == 0):
                zeroError += 1
                if ((not triggerTerminate) and (zeroError == totalTerm)):
                    termMsg = "Terminated by zero error achieved"
                    triggerTerminate = True

        if view:
            print("Error: ", end="")
            printArray(errX, roundV, postfix="%")
            print("\n")

        # Stop if there exist tolerable error
        if (triggerTerminate):
            # Save the Result
            iteration = k+1
            arrOut = x_val
            errEnd = errX
            break

        # Save if Limit
        if (k == limit - 1):
            termMsg = "Terminated by Limit of iteration"
            iteration = k+1
            arrOut = x_val
            errEnd = errX

    print(termMsg)
    print("Result: ", end="")
    printArray(x_val, roundV)
    print()
    print("Error : ", end="")
    printArray(errEnd, roundV)
    print()

    return [arrOut, iteration]


# Power Regressor, Array Formulator
def powerRegressor(x_val=[], y_val=[], power=1):
    # Exception Handler
    if len(x_val) != len(y_val):
        print("Invalid input! Cannot regress different size of x_val and y_val!")
        return

    # Evaluate Matrix
    # Take the n
    n_val = len(x_val)  # Bascially the same as len(y_val)
    matrix = []

    # Iterate through matrix
    for i in range(power):
        vector = []

        # Iterate through vector
        for j in range(power):
            # Only append if it's not the very first element
            if (i == 0 and j == 0):
                vector.append(n_val)
                continue

            # Iterate through sum
            sum = 0
            for k in range(len(x_val)):
                # Sigma of x_val^(row+col)
                sum += x_val[k]**(i+j)

            vector.append(sum)

        matrix.append(vector)

    # Test
    # print("Matrix:")
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[i])):
    #         print(matrix[i][j], end="\t\t")
    #     print()

    # Evaluate Res_Vector
    res_vector = []

    # Iterate through y
    for i in range(power):
        sum = 0
        # Sum each power
        for j in range(len(y_val)):
            # Component y & x
            y_comp = y_val[j]
            x_comp = x_val[j]**(i)
            # Sum
            sum += y_comp * x_comp
        # Append vector
        res_vector.append(sum)

    # Test
    # print("Vector:")
    # print(res_vector)

    return [matrix, res_vector]


# Setting Up Configurations
# Guess
inputBefVal = 0
inputVal = 0.7

# Round and Tolerance
inputRound = 50
errRound = 5
errTolerance = 1e-50
iterLimit = 10000
gseidMinErrPass = 3

viewProcess = False

# Input Values
x_vector = [0.75, 2, 3, 4, 6, 8, 8.5]
y_vector = [1.2, 1.95, 2, 2.4, 2.4, 2.7, 2.6]

switch = True
if (switch):
    # Calling Methods for Power Regressor
    matrixPR, vectorPR = powerRegressor(
        x_val=(x_vector), y_val=(y_vector), power=(3))
    guessPR = [0, 0, 0]

    # Calling Methods for Linear Algebra Solving
    gaussSeidRes, gaussSeidIter = GaussSeidel(roundV=(inputRound), errTol=(errTolerance), totalTerm=(
        gseidMinErrPass), b_val=(vectorPR), x_val=(guessPR), matrix=(matrixPR), limit=(iterLimit), view=(viewProcess))
    print()

    # Convert Result to Function
    funcYes = arrToFunc(gaussSeidRes)

    # Calling Methods Root-Finding
    newtRaphRes, newtRaphIter = NewtonRaphson(f=(funcYes), f_dif=(diff(funcYes, x)), val=(inputVal), roundV=(
        inputRound), errRound=(errRound), tolerance=(errTolerance), limit=(iterLimit), view=(viewProcess))
    print()
    secnMthdRes, secnMthdIter = SecantMethod(valCurr=(inputVal), valBef=(inputBefVal), roundV=(
        inputRound), errRound=(errRound), tolerance=(errTolerance), f=(funcYes), limit=(iterLimit), view=(viewProcess))
    print()

    # Making Up Conclusions:
    print() if viewProcess else 0
    print("[Evaluation finished with the result]")
    print(f"Analyzing the dataset of:\n",
          f"x = {x_vector}\n",
          f"y = {y_vector}\n")

    print("Analysis of Regressor:")
    print(
        f"Gauss  Seidel  resulted in the vector of:\t\t{gaussSeidRes} with {gaussSeidIter} iterations.")
    print(
        f"Translated into Power Regressor in a function of:\t{funcYes}", end="\n\n")
    print("Analysis of Root:")
    print(
        f"Newton Raphson resulted in:\t\t\t\t{newtRaphRes} with {newtRaphIter} iterations.")
    print(
        f"Secant Method  resulted in:\t\t\t\t{secnMthdRes} with {secnMthdIter} iterations.")
    print("[Evaluation completed]")
