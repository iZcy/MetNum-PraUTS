from NewtonRaphson import *
from SecantMethod import *
from GaussSeidel import *
from PowerRegressor import *
from Config import *
from InputX import x_vector
from InputY import y_vector

# Execute Function


def PowRegProcess(inputVectX=[], inputVectY=[], power=regressPower):
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


def GauSedProcess(matrixPR, vectorPR, convertFunc=True):
    # Calling Methods for Linear Algebra Solving
    
    # Default minError = as much as vector elements
    minErr = 0
    if gseidMinErrPass > 0:
        minErr = gseidMinErrPass
    else:
        minErr = len(vectorPR)

    gaussSeidRes, gaussSeidIter = GaussSeidel(roundV=(inputRound), errTol=(errTolerance), totalTerm=(
        minErr), b_val=(vectorPR), guess=(inputGuess if inputGuess else 0), matrix=(matrixPR), limit=(iterLimit), view=(viewProcess))

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
