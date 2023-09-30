import copy
from Processors import *
from InputFunction import *

def analysis(gaussSeidRes, gaussSeidIter, fixedFunction, newtRaphRes, newtRaphIter, secnMthdRes, secnMthdIter, isRootFinding, isLinEqSlving, isEqRegressor):
    # Making Up Conclusions:
    if (isEqRegressor):
        print("[Evaluation finished with the result]\n")
        print(f"Analyzing the dataset of:\n",
              f"x = {val_x}\n",
              f"y = {val_y}\n")
        print("Analysis of Regressor:")

    if (isLinEqSlving or isEqRegressor):
        print(
            f"Gauss  Seidel  resulted in the vector of:\n{gaussSeidRes}\nwith {gaussSeidIter} iterations.\n")
        if (isEqRegressor):
            print(
                f"Translated into Power Regressor in a function of:\n{fixedFunction}", end="\n\n")

    if (isRootFinding):
        print("Analysis of Root:")
        print(
            f"Newton Raphson resulted in:\n{newtRaphRes}\nwith {newtRaphIter} iterations.")
        print(
            f"Secant Method  resulted in:\n{secnMthdRes}\nwith {secnMthdIter} iterations.")
        print("\n[Evaluation completed]")


def execute(isRootFinding, isLinEqSlving, isEqRegressor):
    # Calling PowerReg
    matrixPR = []
    vectorPR = []
    if (isEqRegressor):
        matrix, vector = PowRegProcess()
        matrixPR = copy.deepcopy(matrix)
        vectorPR = copy.deepcopy(vector)

    # Calling GaussSed
    fixedFunction = funct
    gaussSeidRes = []
    gaussSeidIter = 0
    if (isLinEqSlving or isEqRegressor):
        if (isEqRegressor):
            func, gaussSdRes, gaussSdIter = GauSedProcess(matrixPR, vectorPR)
        else:
            func, gaussSdRes, gaussSdIter = GauSedProcess(
                matrixIn, vectorIn, convertFunc=(False))

        fixedFunction = func
        gaussSeidRes = copy.deepcopy(gaussSdRes)
        gaussSeidIter = gaussSdIter

    # Calling RootFind
    newtRaphRes = []
    newtRaphIter = 0
    secnMthdRes = []
    secnMthdIter = 0

    if (isRootFinding):
        newtRhRes, newtRIter, secnMRes, secnMIter = SrRootProcess(fixedFunction)
        newtRaphRes = copy.deepcopy(newtRhRes)
        newtRaphIter = newtRIter
        secnMthdRes = copy.deepcopy(secnMRes)
        secnMthdIter = secnMIter

    analysis(fixedFunction=(fixedFunction), gaussSeidIter=(gaussSeidIter), gaussSeidRes=(gaussSeidRes), newtRaphIter=(
        newtRaphIter), newtRaphRes=(newtRaphRes), secnMthdIter=(secnMthdIter), secnMthdRes=(secnMthdRes), isRootFinding=(isRootFinding), isLinEqSlving=(isLinEqSlving), isEqRegressor=(isEqRegressor))