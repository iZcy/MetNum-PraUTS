import os
import copy
from Output import *

# User Interface
def u_interface_select():
    return input("Choose: ")


def u_interface_wlcm():  # Welcome
    print("Welcome to Numerical Method Analysis Program")


options_type = [
    "Please choose your Numerical Method Type:",
    "Root-Finding",
    "Linear Equation Solver",
    "Equation Regressor"
]

options_input = [
    "Pleace choose your input:",
    "From Input file",
    "From manual input"
]


def optionHandler(options=[], taken=[], chosen=""):  # Reduce Options
    selected = copy.deepcopy(taken)

    # Check selection validity
    if (chosen != "") and (chosen in options):
        # Pick Regress = Pick Gauss
        if (chosen == options_type[3] and options_type[2] in options):
            selected.append(options_type[2])
            options.remove(options_type[2])

        selected.append(chosen)
        options.remove(chosen)
    else:
        # Choice is either invalid or the options are empty.
        print("Invalid request!")
        return [False, False]

    # Test
    # print("Opts: ", options, "\nSlct: ", selected)

    return [options, selected]


def optionDisplayer(options=[], selected=[], multiChoice=True):  # Display Options
    if len(options) <= 1:
        print("Cannot proceed to the next process as there is no option available!")
        return [False, False]

    localOpts = copy.deepcopy(options)
    localSlct = copy.deepcopy(selected)

    while True:
        # Handle Interface Output
        print(localOpts[0])
        for i in range(len(localOpts)-1):
            print(i+1, ") ", localOpts[i+1], sep="")

        if localSlct != []:
            print("x) Finish Selection")

        # Input Handler
        inputVal = u_interface_select()

        if (localSlct != [] and inputVal == "x"):
            break

        try:  # Conversion Handler
            inputVal = int(inputVal)
        except:
            os.system('cls')
            print("Your input is not a number! Please try again!")
            continue

        if inputVal <= 0 or inputVal >= len(localOpts):  # Range Handler
            os.system('cls')
            print("Your input is out of range! Please try again!")
            continue

        # Process Input
        handledOpts, handledSelect = optionHandler(
            options=(localOpts), taken=(localSlct), chosen=(localOpts[inputVal]))  # Update Options

        # Save Input
        localOpts = handledOpts
        localSlct = handledSelect

        os.system('cls')

        # Break if not multiChoice
        if not multiChoice:
            break

        # Break if no options left
        if len(localOpts) <= 1:
            break

    os.system('cls')
    return [handledOpts, handledSelect]


def u_interface_mthd(callback_input):  # Numerical Method Type
    options, selected = optionDisplayer(options_type)

    # Test
    # print("Opts", options)
    # print("Sclt", selected)

    # Booleans
    isRootFinding = options_type[1] in selected
    isLinEqSlving = options_type[2] in selected
    isEqRegressor = options_type[3] in selected

    manualInput = callback_input()

    # Selectors
    if (isRootFinding and isLinEqSlving and isEqRegressor):
        print(
            "You're choosing: Data Set -> Power Regression --[GS]--> Function --[NR, SM]--> Root")
    elif (isRootFinding and isLinEqSlving):
        print("You're choosing: Matrix --[GS]--> Function --[NR, SM]--> Root")
    elif (isRootFinding and isEqRegressor):
        print("You're choosing: (there is no supporting method for this one)")
    elif (isLinEqSlving and isEqRegressor):
        print(
            "You're choosing: Dataset --> Power Regression --[GS]--> Function")
    elif (isRootFinding):
        print("You're choosing: Root Finding [NR, SM]")
    elif (isLinEqSlving):
        print("You're choosing: Linear Equation Solving [GS]")
    elif (isEqRegressor):
        print("You're choosing: Equation Regression [Power+GS]")
    else:
        print("ERROR IN METHOD CHOICE SELECTION")

    print()

    execute(isRootFinding=(isRootFinding), isLinEqSlving=(
        isLinEqSlving), isEqRegressor=(isEqRegressor), manualInput={manualInput})


def u_interface_src():  # Data Source
    options, selected = optionDisplayer(options_input, multiChoice=(False))

    # Booleans
    isFromFile = options_input[1] in selected
    isManualIn = options_input[2] in selected

    # Selectors
    if (isFromFile):
        print("You're choosing: Exported Input")
        return False
    elif (isManualIn):
        print("You're choosing: Manual Input")
        return True
    else:
        print("ERROR IN SOURCE CHOICE SELECTION")

    print()


def u_interface():
    u_interface_wlcm()
    u_interface_mthd(callback_input=(u_interface_src))