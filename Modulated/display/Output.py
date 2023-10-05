from sympy import *
import copy
import os

from middleware.Processors import *
from middleware.ExtraFunction import *
from middleware.DataValidity import *

from inputFiles.InputFunction import *
from inputFiles.InputGauss import inMatrix, inVector
from inputFiles.InputX import x_vector
from inputFiles.InputY import y_vector

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
            func, gaussSdRes, gaussSdIter = GauSedProcess(matrixPR, vectorPR, convertFunc=(convertToFunc))
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
            inputMin = mustNumber("Please input minimum restriction: ", dataType="float")
            inputMax = mustNumber("Please input maximum restriction: ", dataType="float")

            newtRhRes, newtRIter, secnMRes, secnMIter = SrRootProcess(fixedFunction, intervalMin=(inputMin), intervalMax=(inputMax))

        else:
            newtRhRes, newtRIter, secnMRes, secnMIter = SrRootProcess(fixedFunction)
          
        newtRaphRes = copy.deepcopy(newtRhRes)
        newtRaphIter = newtRIter
        secnMthdRes = copy.deepcopy(secnMRes)
        secnMthdIter = secnMIter

    # print("Fix", fixedFunction, "Real", realFunction, sep="\n")
    analysis(fixedFunction=(fixedFunction), realFunction=(realFunction), gaussSeidIter=(gaussSeidIter), gaussSeidRes=(gaussSeidRes), newtRaphIter=(
        newtRaphIter), newtRaphRes=(newtRaphRes), secnMthdIter=(secnMthdIter), secnMthdRes=(secnMthdRes), isRootFinding=(isRootFinding), isLinEqSlving=(isLinEqSlving), isEqRegressor=(isEqRegressor), manualInput=(inputManual), x_data=(matrixPR), y_data=(vectorPR), isOptimization=(isOptimization))
