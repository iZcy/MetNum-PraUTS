from NewtonRaphson import *
from SecantMethod import *
from GaussSeidel import *
from PowerRegressor import *
from Config import *

# Execute Function
def PowRegProcess():
    # Calling Methods for Power Regressor
    matrixPR, vectorPR = PowerRegressor(
        x_val=(val_x), y_val=(val_y), power=(regressPower))

    # print(matrixPR)
    # print(vectorPR)

    return [matrixPR, vectorPR]


def GauSedProcess(matrixPR, vectorPR, convertFunc=True):
    # Calling Methods for Linear Algebra Solving
    gaussSeidRes, gaussSeidIter = GaussSeidel(roundV=(inputRound), errTol=(errTolerance), totalTerm=(
        gseidMinErrPass), b_val=(vectorPR), guess=(inputGuess if inputGuess else 0), matrix=(matrixPR), limit=(iterLimit), view=(viewProcess))

    if gaussSeidIter == 0:
        return
    print()

    # Convert Result to Function
    fixedFunction = 0
    if convertFunc:
        fixedFunction = arrToFunc(gaussSeidRes)

    return [fixedFunction, gaussSeidRes, gaussSeidIter]


def SrRootProcess(fixedFunction):
    # Calling Methods Root-Finding
    newtRaphRes, newtRaphIter = NewtonRaphson(f=(fixedFunction), f_dif=(diff(fixedFunction, x)), val=(inputVal), roundV=(
        inputRound), errRound=(errRound), tolerance=(errTolerance), limit=(iterLimit), view=(viewProcess))
    print()
    secnMthdRes, secnMthdIter = SecantMethod(valCurr=(inputVal), valBef=(inputBefVal), roundV=(
        inputRound), errRound=(errRound), tolerance=(errTolerance), f=(fixedFunction), limit=(iterLimit), view=(viewProcess))
    print()

    return [newtRaphRes, newtRaphIter, secnMthdRes, secnMthdIter]
