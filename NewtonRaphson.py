from ExtraFunction import *

# NewtonRaphson
def NewtonRaphson(f, f_dif, val, roundV, errRound, tolerance=0.00001, limit=1000, it=0, errPrev=0, view=True):
    # Intializing Process
    if (it == 0):
        print("Start to evaluate Newton Raphson")

    # Simulation Terminator: Limit of Loop
    if (it == limit):
        print(
            "Iteration Limit! The function is either divergent or requires more iteration!")
        return [val, it]

    # Newton Raphson Formula + Error Evaluation
    value = val - evToX(f, val) / evToX(f_dif, val)
    error = (value - val)/value

    if view:
        print("Iterate: ", it+1, "\tPrevious: ", val, "\tCurrent: ",
              value, "\tError: ", round(error*100, errRound), "%")

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
    elif (round(val, roundV) == round(value, roundV)):
        print("Stopped by the tolerated round value")
        terminate = True

    # Terminator
    if terminate:
        print("Newton Raphson Stopped! Last Value:", value)
        return [val, it]

    return NewtonRaphson(f, f_dif, value, roundV, errRound,
                         tolerance, limit, iter, error, view)