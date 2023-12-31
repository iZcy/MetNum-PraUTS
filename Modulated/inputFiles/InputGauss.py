inMatrix = [
    [3, -0.1, -0.2],
    [0.1, 7, -0.3],
    [0.3, -0.2, 10],
]

inVector = [
    7.85, -19.3, 71.4
]

# Check Matrix Validity
vctLen = len(inMatrix[0])
for i in range(len(inMatrix) - 1):
  currVctLen = len(inMatrix[i + 1])

  # print(f"Compare {vctLen} vs {currVctLen}")
  if (vctLen != currVctLen):
    print("Inequal inMatrix Size!")
    exit()
  
  vctLen = currVctLen

# Check Vector Validity
if (vctLen != len(inVector)):
  print("Incompatible inVector Size!")
  exit()