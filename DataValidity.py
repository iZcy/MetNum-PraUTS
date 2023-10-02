from Config import *
from InputX import *
from InputY import *


def checkValidity():
    if (len(x_vector) != len(y_vector)):
        print("Data size mismatch!")
        exit()


def checkConfig(resLen):
    # print(f"Len: {resLen} with gseiderr: {gseidMinErrPass} and arrLenGuess: {len(inputGuess)} cond1: {gseidMinErrPass > resLen} and cond2: {len(inputGuess) > resLen}")
    if ((gseidMinErrPass > resLen) or (len(inputGuess) > resLen)):
      
        print("Config size conflicts! Please rematch your config!")
        exit()
