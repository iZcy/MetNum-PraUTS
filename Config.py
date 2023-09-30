from InputX import x_vector
from InputY import y_vector
from InputGauss import inMatrix, inVector

# Setting Up Configurations
# Method Setting
regressPower = 4    # Regressor Power
gseidMinErrPass = 3
# Minimum vector values that pass the error tolerance ex. for val = 2, [0%, 0%, 5%] is considered to as valid to return

# Input Guess
inputBefVal = 0
inputVal = 0.7
inputGuess = []  # n = Regressor power: otherwise, return error
# [alternative: leave as an empty array to automatically make zero vector guess]

# Import Value
val_x = x_vector
val_y = y_vector

matrixIn = inMatrix
vectorIn = inVector

# Round and Tolerance
inputRound = 50
errRound = 10
errTolerance = 0.001
iterLimit = 1000000

# View Toggle
viewProcess = False