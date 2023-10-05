# Setting Up Configurations
# Method Setting
regressPower = 4      # Regressor Power + 1 ex. for 1 degree of x, do 2
gseidMinErrPass = 0   # Default<=0 adjust to the vector size
# Minimum vector values that pass the error tolerance ex. for val = 2, [0%, 0%, 5%] is considered to as valid to return

# Input Guess
inputBefVal = 41
inputVal = 45
inputGuess = []  # n = Regressor power: otherwise, return error
# [alternative: leave as an empty array to automatically make zero vector guess]

# Round and Tolerance
inputRound = 50
errRound = 50
errTolerance = 1e-100
iterLimit = 1000

# Optimization
intervalMin = float('-inf')
intervalMax = float('inf')

# View Toggle
viewProcess = False
#
#
#
#
#
#
#
#
#
#
# IMPORT & Symbols
from sympy import *
import os
import copy

# Creating Methods
x = symbols('x')
#
#
#
#
#
#
#
#
#
#
# INPUT
x_vector = [
    0,
    1,
    1.7071067811865
]

y_vector = [
    1,
    -1,
    0
]

inMatrix = [
    [3, -0.1, -0.2],
    [0.1, 7, -0.3],
    [0.3, -0.2, 10],
]

inVector = [
    7.85, -19.3, 71.4
]

funct = "-2*x**2 + 3*x + 1"

try:
  funct = sympify(funct)
except:
  print("Invalid Function Input!")
  exit()

# Check Matrix Validity
vctLen = len(inMatrix[0])
for i in range(len(inMatrix) - 1):
  currVctLen = len(inMatrix[i + 1])

  # print(f"Compare {vctLen} vs {currVctLen}")
  if (vctLen != currVctLen):
    print("Inequal inMatrix Size!")
    exit()
  
  vctLen = currVctLen

# Check Vector Validity
if (vctLen != len(inVector)):
  print("Incompatible inVector Size!")
  exit()

#
#
#
#
#
#
#
#
#
#
# NUMERICAL METHODS
# Gauss-Seidel
def GaussSeidel(roundV, errTol, totalTerm, b_val, matrix, guess=0, limit=100, view=True):
    # Exception Handler
    if (guess != 0 and (len(guess) != len(b_val))):
        print("Inequal length of 'guess-vector' and 'y-vector'\n",
              "Terminating the whole process!", sep="")
        return [0, 0]

    # Init Message
    print("Start to Evaluate Gauss Seidel Method")

    # Init Values
    iteration = 0
    arrOut = []
    errEnd = []

    errX = []
    x_valProcess = []

    # print(b_val, "\n", matrix)

    # Guess-Handler
    if (guess == 0):  # If it is not set, set all to zero
        for i in range(len(b_val)):
            errX.append(0)
        x_valProcess = copy.deepcopy(errX)
    else:  # If it is set, copy it to process and error comparison
        x_valProcess = guess
        errX = copy.deepcopy(guess)

    # Loop the Gauss-Seidel
    for k in range(limit):
        # Terminate Message
        termMsg = ""

        if view:
            print("Loop :", k+1, "\nBefore: ", end="")

            # Current value Display
            printArray(x_valProcess, roundV)

            print()

        # Single Gauss-Seidel Process
        prev_x_valProcess = copy.deepcopy(x_valProcess)
        for j in range(len(matrix)):
            val = 0
            # Adding value to the b-value
            # print("Add", b[j])
            val += b_val[j]

            for i in range(len(matrix[j])-1):
                index = (j + 1 + i) % len(matrix[j])
                # Subtracting the value to x vars with response to the DYNAMIC x-input
                # print(-vars[j][index], "x" + str(index+1))
                val -= matrix[j][index] * x_valProcess[index]

            # Dividing the value to the analyzed x-output
            # print("Div by", vars[j][j])
            val /= matrix[j][j]

            # Move value to the storage
            x_valProcess[j] = val

        # Error Calculation
        triggerTerminate = False

        # Error Tolerance Count
        toleratedError = 0
        zeroError = 0

        if view:
            print("Current: ", end="")

            # Current value Display
            printArray(x_valProcess, roundV)
            print()

        for i in range(len(errX)):
            errX[i] = 0
            try:
              errX[i] = abs((x_valProcess[i] - prev_x_valProcess[i]) /
                            x_valProcess[i])*100
            except:
              errX[i] = 0

            # Terminate if the minimum error achieved
            if (abs(errX[i]) < errTol):
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
            arrOut = x_valProcess
            errEnd = errX
            break

        # Save if Limit
        if (k == limit - 1):
            termMsg = "Terminated by Limit of iteration"
            iteration = k+1
            arrOut = x_valProcess
            errEnd = errX

    print(termMsg)
    print("Result: ", end="")
    printArray(x_valProcess, roundV)
    print()
    print("Error : ", end="")
    printArray(errEnd, roundV, postfix="%")
    print()

    return [arrOut, iteration]

# NewtonRaphson
def NewtonRaphson(f, f_dif, val, roundV, errRound, tolerance=0.00001, limit=1000, view=True, intervalMin=float('-inf'), intervalMax=float('-inf')):
    iter = 0
    errPrev = 0
    currentVal = val

    for it in range(limit):
        iter = it + 1
        # Intializing Process
        if (it == 0):
            print("Start to evaluate Newton Raphson")
        
        # Newton Raphson Formula + Error EcurrentValuation
        currentValue = currentVal - evToX(f, currentVal) / evToX(f_dif, currentVal)
        error = (currentValue - currentVal)/currentValue

        if view:
            print("Iterate: ", it+1, "\tPrevious: ", currentVal, "\tCurrent: ",
                  currentValue, "\tError: ", round(error*100, errRound), "%")

        # Updating Process
        terminate = False

        errorStop = False # To allow linear functions be able to determined
        try:
          abs(error - errPrev) < tolerance
        except:
          0

        # Simulation Terminator: Interval exceeding --- Exceeds the restriction
        if ((intervalMin != float('-inf') and intervalMax != float('inf')) and (currentValue < intervalMin or currentValue > intervalMax)):
            print("Stopped by the restricted interval exceeded")
            if (currentValue < intervalMin):
                currentValue = intervalMin
            elif (currentValue > intervalMax):
                currentValue = intervalMax
                
            return [currentValue, iter]

        # Simulation Terminator: Found --- 0 Error a.k.a currentValue is found
        if (error == 0):
            print("Stopped by the exact currentValue found")
            terminate = True

        # Simulation Terminator: Error Tolerance --- Error difference is too small to continue
        elif (it != 0 and errorStop):
            print("Stopped by the error tolerance limit")
            terminate = True

        # Simulation Terminator: Almost exact --- Change of currentValue is too small to continue
        elif (round(currentVal, roundV) == round(currentValue, roundV)):
            print("Stopped by the tolerated round currentValue")
            terminate = True

        # Simulation Terminator: Found!
        elif (evToX(f, currentValue) == 0.0):
            print("Solution found!")
            terminate = True

        # Continue Update
        currentVal = currentValue

        # Terminator
        if terminate:
            print("Newton Raphson Stopped! Last currentValue:", currentValue)
            return [currentVal, iter]
    
    # Simulation Terminator: Limit of Loop
    print("Iteration Limit! The function is either divergent or requires more iteration!")
    return [currentVal, iter]

# Power Regressor, Array Formulator
def PowerRegressor(x_val=[], y_val=[], power=1):
    # Exception Handler
    if len(x_val) != len(y_val):
        print("Invalid input! Cannot regress different size of x_val and y_val!")
        exit()

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

# Secant Method


def SecantMethod(f, valCurr, valBef, roundV, errRound, tolerance=0.00001, limit=1000, view=True, intervalMin=float('-inf'), intervalMax=float('-inf')):
    iter = 0
    errPrev = 0

    currentVal = valCurr
    current2ndVal = valBef

    for it in range(limit):
        iter = it + 1

        # Intializing Process
        if (it == 0):
            print("Start to evaluate Secant Method")

        # Secant Method Formula + Error Evaluation
        valUpd = currentVal - (
            evToX(f, currentVal) * (
                current2ndVal - currentVal
            )
        ) / (
            evToX(f, current2ndVal) - evToX(f, currentVal)
        )
        error = (valUpd - currentVal)/valUpd

        if view:
            print("Iterate: ", it+1, "\tPrevious: ", currentVal, "\tCurrent: ",
                  valUpd, "\tError: ", round(error*100, errRound), "%")

        # Updating Process
        terminate = False

        # Simulation Terminator: Interval exceeding --- Exceeds the restriction
        if ((intervalMin != float('-inf') and intervalMax != float('inf')) and (valUpd < intervalMin or valUpd > intervalMax)):
            print("Stopped by the restricted interval exceeded")
            if (valUpd < intervalMin):
                valUpd = intervalMin
            elif (valUpd > intervalMax):
                valUpd = intervalMax
                
            return [valUpd, iter]

        # Simulation Terminator: Found --- 0 Error a.k.a value is found
        if (error == 0):
            print("Stopped by the exact value found")
            terminate = True

        # Simulation Terminator: Error Tolerance --- Error difference is too small to continue
        elif (it != 0):
            try:
                if (abs(error - errPrev) < tolerance):
                    print("Stopped by the error tolerance limit")
                    terminate = True
            except:
                0

        # Simulation Terminator: Almost exact --- Change of value is too small to continue
        elif (round(currentVal, roundV) == round(valUpd, roundV)):
            print("Stopped by the tolerated round value")
            terminate = True

        # Simulation Terminator: Found!
        elif (evToX(f, valUpd) == 0.0):
            print("Solution found!")
            terminate = True

        # Continue Update
        current2ndVal = currentVal
        currentVal = valUpd

        # Terminator
        if terminate:
            print("Secant Method Stopped!  Last Value:", valUpd)
            return [round(valUpd, roundV), iter]

    # Simulation Terminator: Limit of Loop
    print("Iteration Limit! The function is either divergent or requires more iteration!")
    return [round(currentVal, roundV), iter]

#
#
#
#
#
#
#
#
#
#
# MIDDLEWARE --- [Data Validation]
def checkValidity():
    if (len(x_vector) != len(y_vector)):
        print("Data size mismatch!")
        exit()


def checkConfig(resLen):
    # print(f"Len: {resLen} with gseiderr: {gseidMinErrPass} and arrLenGuess: {len(inputGuess)} cond1: {gseidMinErrPass > resLen} and cond2: {len(inputGuess) > resLen}")
    if ((gseidMinErrPass > resLen) or (len(inputGuess) > resLen)):
      
        print("Config size conflicts! Please rematch your config!")
        exit()

# MIDDLEWARE --- [Extra Function]
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

# MIDDLEWARE --- [Processors]
# Execute Function
def PowRegProcess(inputVectX=[], inputVectY=[], power=regressPower):
    os.system('cls')
    # Calling Methods for Power Regressor
    if (inputVectX != [] and inputVectY != []):
        matrixPR, vectorPR = PowerRegressor(
            x_val=(inputVectX), y_val=(inputVectY), power=(power))
    else:
        matrixPR, vectorPR = PowerRegressor(
            x_val=(x_vector), y_val=(y_vector), power=(power))

    # print(matrixPR)
    # print(vectorPR)

    return [matrixPR, vectorPR]


def GauSedProcess(matrixPR, vectorPR, convertFunc=True, guess=(inputGuess if inputGuess else 0), errTol=(errTolerance)):
    os.system('cls')
    # Calling Methods for Linear Algebra Solving
    
    # Default minError = as much as vector elements
    minErr = 0
    if gseidMinErrPass > 0:
        minErr = gseidMinErrPass
    else:
        minErr = len(vectorPR)

    gaussSeidRes, gaussSeidIter = GaussSeidel(roundV=(inputRound), errTol=(errTol), totalTerm=(
        minErr), b_val=(vectorPR), guess=(guess), matrix=(matrixPR), limit=(iterLimit), view=(viewProcess))

    if gaussSeidIter == 0:
        return
    print()

    # Convert Result to Function
    fixedFunction = 0
    if convertFunc:
        fixedFunction = arrToFunc(gaussSeidRes)

    return [fixedFunction, gaussSeidRes, gaussSeidIter]


def SrRootProcess(fixedFunction, intervalMin=(intervalMin), intervalMax=(intervalMax), guessOne=(inputVal), guessTwo=(inputBefVal), errTol=(errTolerance)):
    os.system('cls')
    # Calling Methods Root-Finding
    newtRaphRes, newtRaphIter = NewtonRaphson(f=(fixedFunction), f_dif=(diff(fixedFunction, x)), val=(guessOne), roundV=(
        inputRound), errRound=(errRound), tolerance=(errTol), limit=(iterLimit), view=(viewProcess), intervalMin=(intervalMin), intervalMax=(intervalMax))
    print()
    secnMthdRes, secnMthdIter = SecantMethod(valCurr=(guessOne), valBef=(guessTwo), roundV=(
        inputRound), errRound=(errRound), tolerance=(errTol), f=(fixedFunction), limit=(iterLimit), view=(viewProcess), intervalMin=(intervalMin), intervalMax=(intervalMax))
    print()

    return [newtRaphRes, newtRaphIter, secnMthdRes, secnMthdIter]

#
#
#
#
#
#
#
#
#
#
# DISPLAY --- [Output]
def analysis(gaussSeidRes, gaussSeidIter, fixedFunction, realFunction, newtRaphRes, newtRaphIter, secnMthdRes, secnMthdIter, isRootFinding, isLinEqSlving, isEqRegressor, manualInput=False, x_data=[], y_data=[], isOptimization = False):
    # Setup Import
    analyzeX = x_vector
    analyzeY = y_vector

    if manualInput:
        analyzeX = x_data
        analyzeY = y_data

    # Making Up Conclusions:
    if (isEqRegressor):
        print("[Evaluation finished with the result]\n")
        # print(f"Analyzing the dataset of:\n",
        #       f"x = {analyzeX}\n",
        #       f"y = {analyzeY}\n")
        print("Analysis of Regressor:")

    if (isLinEqSlving or isEqRegressor):
        print(
            f"Gauss  Seidel  resulted in the vector of:\n{gaussSeidRes}\nwith {gaussSeidIter} iterations.\n")
        if (isEqRegressor):
            print(
                f"Translated into Power Regressor in a function of:\n{fixedFunction}", end="\n\n")

    if (isRootFinding):
        print("Analysis of Root:")
        
        if (isOptimization):
            print("\n(Optimization Mode)\n")

        print(
            f"Newton Raphson resulted in:\n{newtRaphRes}\nwith {newtRaphIter} iterations.")

        if (isOptimization):
            print("Max/min Value:", evToX(realFunction, newtRaphRes))
        
        print(
            f"Secant Method  resulted in:\n{secnMthdRes}\nwith {secnMthdIter} iterations.")

        if (isOptimization):
            print("Max/min Value:", evToX(realFunction, secnMthdRes))
        print("\n[Evaluation completed]")


def execute(isRootFinding, isLinEqSlving, isEqRegressor, manualInput, isOptimization = False):
    # print(f"{isRootFinding}, {isLinEqSlving}, {isEqRegressor}, {inputManual}")
    convertToFunc = False
    inputManual = list(manualInput)[0]

    # Setting Error Tolerance
    errTol = 0
    if (inputManual):
        errTol = mustNumber("Please input error tolerance: ", dataType=("float"))
    os.system('cls')

    # Calling PowerReg
    matrixPR = []
    vectorPR = []
    if (isEqRegressor and not inputManual):
        matrix, vector = PowRegProcess()
        matrixPR = copy.deepcopy(matrix)
        vectorPR = copy.deepcopy(vector)
        convertToFunc = True

    # Function Definition
    fixedFunction = funct
    realFunction  = funct

    while (True and inputManual and isRootFinding and not isLinEqSlving):
        tempFunct = input("Please input your function: ")

        passed = False
        try:
            tempFunct = sympify(tempFunct)
            round(evToX(tempFunct, 1), 1)
            passed = True
        except:
            os.system('cls')
            print("Your input is not a valid function!")

        if (passed):
            fixedFunction = tempFunct
            realFunction  = tempFunct
            break

    # Calling GaussSed

    gaussSeidRes = []
    gaussSeidIter = 0

    if (inputManual):
        if (isLinEqSlving):
            repeatX = mustNumber(
                "Please input your data row: ", dataType="int")
            repeatY = mustNumber(
                "Please input your data col: ", dataType="int")
            for i in range(repeatY):
                tempVector = []
                for k in range(repeatX):
                    os.system('cls')
                    print("Current matrix:")
                    printMatrix(matrixPR, 2)
                    print(f"Current vector:\n{tempVector}")

                    tempInput = 0
                    tempInput = mustNumber(f"Please input the value of ({i}, {k}): ", errMsg=(
                        f"Current vector:\n{tempVector}"))
                    tempVector.append(tempInput)
                matrixPR.append(tempVector)

            for i in range(repeatX):
                os.system('cls')
                print("Completed matrix:")
                printMatrix(matrixPR, 2)
                print(f"Current output vector:\n{vectorPR}")
                tempInput = mustNumber(f"Please input the output number {i}: ", loopMsg=(
                    f"Completed Matrix:\n{matrixPR}\nCurrent output vector:\n{vectorPR}"))
                vectorPR.append(tempInput)

            os.system('cls')
            print("Completed matrix:")
            printMatrix(matrixPR, 2)
            print(f"Current output vector:\n{vectorPR}")

        elif (isEqRegressor):
            inputX = 0
            inputY = 0
            data = []
            vectX = []
            vectY = []

            while True or (len(data) < 2):
                breaking = False
                
                os.system('cls')
                print("Your Data (x, y):")
                printMatrix(data, roundV=2)

                currVect = []
                inputX = mustNumber(
                    "Please input your x-data\nInput 'x' to stop (min. 2 contents).\nData: ", dataType="float", accept=['x'])
                if inputX == 'x':
                    breaking = True
                    if (len(data) >= 2):
                        break

                currVect.append(inputX)

                inputY = mustNumber(
                    "Please input your y-data\nInput 'x' to stop (min. 2 contents).\nData: ", dataType="float", accept=['x'])
                if inputY == 'x':
                    breaking = True
                    if (len(data) >= 2):
                        break

                currVect.append(inputY)

                if (not breaking):
                    data.append(currVect)
                    vectX.append(inputX)
                    vectY.append(inputY)
            
            power = mustNumber("Please input your power rate: ", dataType="unsigned")

            matrix, vector = PowRegProcess(inputVectX=(vectX), inputVectY=(vectY), power=(power+1))
            matrixPR = copy.deepcopy(matrix)
            vectorPR = copy.deepcopy(vector)
            convertToFunc = True

    if ((isLinEqSlving) or (isEqRegressor)):
        if (isLinEqSlving and isRootFinding):
            convertToFunc = True

        if (inputManual or isEqRegressor):
            checkConfig(len(vectorPR))

            guess = 0 # Fill the guess
            if (isLinEqSlving and inputManual):
                guess = []

                for i in range(len(vectorPR)):
                    os.system('cls')
                    print(f"Current guess: {vectorPR}")
                    tempInput = mustNumber(f"Please input the guess number {i}: ", loopMsg=(
                        f"Current guess: {vectorPR}"))
                    guess.append(tempInput)

            func, gaussSdRes, gaussSdIter = GauSedProcess(matrixPR, vectorPR, convertFunc=(convertToFunc), guess=(guess), errTol=(errTol))
        else:
            checkConfig(len(inVector))
            func, gaussSdRes, gaussSdIter = GauSedProcess(inMatrix, inVector, convertFunc=(convertToFunc))

        fixedFunction = func
        realFunction  = func

        gaussSeidRes = copy.deepcopy(gaussSdRes)
        gaussSeidIter = gaussSdIter

    # Calling RootFind
    newtRaphRes = []
    newtRaphIter = 0
    secnMthdRes = []
    secnMthdIter = 0

    if (isOptimization): # Differentiate for optimization
        fixedFunction = diff(fixedFunction, x)

    if (isRootFinding):
        if (list(manualInput)[0]):
            guessOne = mustNumber("Please input 1st guess (for NR and SM): ", dataType="float")
            guessTwo = mustNumber("Please input 2nd guess (for SM)       : ", dataType="float")

            inputMin = mustNumber("Please input minimum restriction: ", dataType="float")
            inputMax = mustNumber("Please input maximum restriction: ", dataType="float")

            newtRhRes, newtRIter, secnMRes, secnMIter = SrRootProcess(fixedFunction, intervalMin=(inputMin), intervalMax=(inputMax), guessOne=(guessOne), guessTwo=(guessTwo), errTol=(errTol))

        else:
            newtRhRes, newtRIter, secnMRes, secnMIter = SrRootProcess(fixedFunction)
          
        newtRaphRes = copy.deepcopy(newtRhRes)
        newtRaphIter = newtRIter
        secnMthdRes = copy.deepcopy(secnMRes)
        secnMthdIter = secnMIter

    # print("Fix", fixedFunction, "Real", realFunction, sep="\n")
    analysis(fixedFunction=(fixedFunction), realFunction=(realFunction), gaussSeidIter=(gaussSeidIter), gaussSeidRes=(gaussSeidRes), newtRaphIter=(
        newtRaphIter), newtRaphRes=(newtRaphRes), secnMthdIter=(secnMthdIter), secnMthdRes=(secnMthdRes), isRootFinding=(isRootFinding), isLinEqSlving=(isLinEqSlving), isEqRegressor=(isEqRegressor), manualInput=(inputManual), x_data=(matrixPR), y_data=(vectorPR), isOptimization=(isOptimization))

# DISPLAY --- [Interface]
# User Interface
def u_interface_select():
    return input("Choose: ")


def u_interface_wlcm():  # Welcome
    print("Welcome to Numerical Method Analysis Program")


options_type = [
    "Please choose your Numerical Method Type:",
    "Root-Finding",
    "Linear Equation Solver",
    "Equation Regressor"
]

options_input = [
    "Please choose your input:",
    "From Input file",
    "From manual input"
]

options_optimization = [
    "Do you wanna use optimization?",
    "Yes",
    "No"
]


def optionHandler(options=[], taken=[], chosen=""):  # Reduce Options
    selected = copy.deepcopy(taken)

    # Check selection validity
    if (chosen != "") and (chosen in options):
        # Pick Regress = Pick Gauss
        # if (chosen == options_type[3] and options_type[2] in options):
        #     selected.append(options_type[2])
        #     options.remove(options_type[2])

        selected.append(chosen)
        options.remove(chosen)
    else:
        # Choice is either invalid or the options are empty.
        print("Invalid request!")
        return [False, False]

    # Test
    # print("Opts: ", options, "\nSlct: ", selected)

    return [options, selected]


def optionDisplayer(options=[], selected=[], multiChoice=True):  # Display Options
    if len(options) <= 1:
        print("Cannot proceed to the next process as there is no option available!")
        return [False, False]

    localOpts = copy.deepcopy(options)
    localSlct = copy.deepcopy(selected)

    while True:
        # Handle Interface Output
        print(localOpts[0])
        for i in range(len(localOpts)-1):
            print(i+1, ") ", localOpts[i+1], sep="")

        if localSlct != []:
            print("x) Finish Selection")

        # Input Handler
        inputVal = u_interface_select()

        if (localSlct != [] and inputVal == "x"):
            break

        try:  # Conversion Handler
            inputVal = int(inputVal)
        except:
            os.system('cls')
            print("Your input is not a number! Please try again!")
            continue

        if inputVal <= 0 or inputVal >= len(localOpts):  # Range Handler
            os.system('cls')
            print("Your input is out of range! Please try again!")
            continue

        # Process Input
        handledOpts, handledSelect = optionHandler(
            options=(localOpts), taken=(localSlct), chosen=(localOpts[inputVal]))  # Update Options

        # Save Input
        localOpts = handledOpts
        localSlct = handledSelect

        os.system('cls')

        # Break if not multiChoice
        if not multiChoice:
            break

        # Break if no options left
        if len(localOpts) <= 1:
            break

    os.system('cls')
    return [handledOpts, handledSelect]


def u_interface_optim():
    options, selected = optionDisplayer(options_optimization, multiChoice=(False))

    decode = True if selected[0] == "Yes" else False if selected[0] == "No" else "Error"

    # print(decode)
    return decode

def u_interface_mthd(callback_input):  # Numerical Method Type
    options, selected = optionDisplayer(options_type)

    # Test
    # print("Opts", options)
    # print("Sclt", selected)

    # Booleans
    isRootFinding = options_type[1] in selected
    isLinEqSlving = options_type[2] in selected
    isEqRegressor = options_type[3] in selected

    manualInput = callback_input()

    # Selectors
    if (isRootFinding and isLinEqSlving and isEqRegressor):
        print(
            "You're choosing: Data Set -> Power Regression --[GS]--> Function --[NR, SM]--> Root")
    elif (isRootFinding and isLinEqSlving):
        print("You're choosing: Matrix --[GS]--> Function --[NR, SM]--> Root")
    elif (isRootFinding and isEqRegressor):
        print("You're choosing: (there is no supporting method for this one)")
    elif (isLinEqSlving and isEqRegressor):
        print(
            "You're choosing: Dataset --> Power Regression --[GS]--> Function")
    elif (isRootFinding):
        print("You're choosing: Root Finding [NR, SM]")
    elif (isLinEqSlving):
        print("You're choosing: Linear Equation Solving [GS]")
    elif (isEqRegressor):
        print("You're choosing: Equation Regression [Power+GS]")
    else:
        print("ERROR IN METHOD CHOICE SELECTION")

    print()

    isOptimiziation = False
    if (isRootFinding):
        isOptimiziation = u_interface_optim()

    execute(isRootFinding=(isRootFinding), isLinEqSlving=(
        isLinEqSlving), isEqRegressor=(isEqRegressor), manualInput={manualInput}, isOptimization=(isOptimiziation))


def u_interface_src():  # Data Source
    options, selected = optionDisplayer(options_input, multiChoice=(False))

    # Booleans
    isFromFile = options_input[1] in selected
    isManualIn = options_input[2] in selected

    # Selectors
    if (isFromFile):
        print("You're choosing: Exported Input")
        return False
    elif (isManualIn):
        print("You're choosing: Manual Input")
        return True
    else:
        print("ERROR IN SOURCE CHOICE SELECTION")

    print()


def u_interface():
    u_interface_wlcm()
    u_interface_mthd(callback_input=(u_interface_src))

# Data Validity
checkValidity()

# Execute
u_interface()