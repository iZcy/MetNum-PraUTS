# Importing Packages
from middleware.DataValidity import checkValidity
from display.Interface import u_interface

try:
    # Data Validity
    checkValidity()

    # Execute
    u_interface()
except:
    print("\nTerminated by Error")