import copy
from ExtraFunction import *

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
            errX[i] = abs((x_valProcess[i] - prev_x_valProcess[i]) /
                          x_valProcess[i])*100

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