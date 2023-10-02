# Power Regressor, Array Formulator
def PowerRegressor(x_val=[], y_val=[], power=1):
    # Exception Handler
    if len(x_val) != len(y_val):
        print("Invalid input! Cannot regress different size of x_val and y_val!")
        exit()

    # Evaluate Matrix
    # Take the n
    n_val = len(x_val)  # Bascially the same as len(y_val)
    matrix = []

    # Iterate through matrix
    for i in range(power):
        vector = []

        # Iterate through vector
        for j in range(power):
            # Only append if it's not the very first element
            if (i == 0 and j == 0):
                vector.append(n_val)
                continue

            # Iterate through sum
            sum = 0
            for k in range(len(x_val)):
                # Sigma of x_val^(row+col)
                sum += x_val[k]**(i+j)

            vector.append(sum)

        matrix.append(vector)

    # Test
    # print("Matrix:")
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[i])):
    #         print(matrix[i][j], end="\t\t")
    #     print()

    # Evaluate Res_Vector
    res_vector = []

    # Iterate through y
    for i in range(power):
        sum = 0
        # Sum each power
        for j in range(len(y_val)):
            # Component y & x
            y_comp = y_val[j]
            x_comp = x_val[j]**(i)
            # Sum
            sum += y_comp * x_comp
        # Append vector
        res_vector.append(sum)

    # Test
    # print("Vector:")
    # print(res_vector)

    return [matrix, res_vector]
