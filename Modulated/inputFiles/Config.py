# Setting Up Configurations
# Method Setting
regressPower = 4      # Regressor Power + 1 ex. for 1 degree of x, do 2
gseidMinErrPass = 0   # Default<=0 adjust to the vector size
# Minimum vector values that pass the error tolerance ex. for val = 2, [0%, 0%, 5%] is considered to as valid to return

# Input Guess
inputBefVal = 41
inputVal = 45
inputGuess = []  # n = Regressor power: otherwise, return error
# [alternative: leave as an empty array to automatically make zero vector guess]

# Round and Tolerance
inputRound = 50
errRound = 50
errTolerance = 1e-100
iterLimit = 1000

# Optimization
intervalMin = float('-inf')
intervalMax = float('inf')

# View Toggle
viewProcess = False