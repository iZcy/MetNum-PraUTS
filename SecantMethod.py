from ExtraFunction import *

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
        print("Stopped by the error tolerance limit")
        terminate = True

    # Simulation Terminator: Almost exact --- Change of value is too small to continue
    elif (round(valCurr, roundV) == round(valUpd, roundV)):
        print("Stopped by the tolerated round value")
        terminate = True

    # Terminator
    if terminate:
        print("Secant Method Stopped!  Last Value:", valUpd)
        return [round(valUpd, roundV), it]

    try:
        return SecantMethod(f, valUpd, valCurr, roundV, errRound, tolerance, limit, iter, error, view)
    except:
        print("Exception Error")
        return ["Failed", "Failed"]