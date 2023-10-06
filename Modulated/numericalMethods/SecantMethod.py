from middleware.ExtraFunction import *

# Secant Method


def SecantMethod(f, valCurr, valBef, roundV, errRound, tolerance=0.00001, limit=1000, view=True, intervalMin=float('-inf'), intervalMax=float('inf')):
    iter = 0
    errPrev = 0

    currentVal = valCurr
    current2ndVal = valBef

    for it in range(int(limit)):
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
