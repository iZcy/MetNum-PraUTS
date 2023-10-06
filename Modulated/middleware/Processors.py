from numericalMethods.NewtonRaphson import *
from numericalMethods.SecantMethod import *
from numericalMethods.GaussSeidel import *
from numericalMethods.PowerRegressor import *

from middleware.ExtraFunction import *

from inputFiles.Config import *
from inputFiles.InputX import x_vector
from inputFiles.InputY import y_vector

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
