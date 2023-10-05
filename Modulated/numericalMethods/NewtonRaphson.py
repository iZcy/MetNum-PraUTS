from middleware.ExtraFunction import *

# NewtonRaphson
def NewtonRaphson(f, f_dif, val, roundV, errRound, tolerance=0.00001, limit=1000, view=True):
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
            terminate = true

        # Continue Update
        currentVal = currentValue

        # Terminator
        if terminate:
            print("Newton Raphson Stopped! Last currentValue:", currentValue)
            return [currentVal, iter]
    
    # Simulation Terminator: Limit of Loop
    print("Iteration Limit! The function is either divergent or requires more iteration!")
    return [currentVal, iter]