import numpy as np
import math

file = open("Day13-Input.txt","r")
data = file.read()

# # Simple case:
# data = """Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176

# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450

# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279"""

def Multiples(one, two):
    temp = one[0] / two[0]
    if temp == math.floor(temp):
        return (one[1]/two[1]) == temp
    return False
    print( np.dot(one,two)*np.dot(one,two) == np.dot(one,one)*np.dot(two,two) )
    return np.dot(one,two)*np.dot(one,two) == np.dot(one,one)*np.dot(two,two)

data = data.split("\n\n")
total = 0
for i, claws in enumerate(data):
    # Data sanitisation
    machines = claws.split("\n")
    machines = [x.replace("Button A: X+","") for x in machines]
    machines = [x.replace("Button B: X+","") for x in machines]
    machines = [x.replace("Prize: X=","") for x in machines]
    machines = [x.split(", Y+") if i != 2 else x.split(", Y=") for i, x in enumerate(machines)]
    machines = [[int(y) for y in x] for x in machines]
    # print(machines)

    # # Set up vectors
    # Part 1:
    # vectorA = np.array(machines[0])
    # vectorB = np.array(machines[1])
    prize = np.array(machines[2])

    # Part 2:
    prize = prize + np.array([10000000000000,10000000000000])


    # Lin alg way:
    basis = np.array([machines[0],machines[1]])
    basis = np.transpose(basis)
    inverseBasis = np.linalg.inv(basis)
    coefficients = np.matmul(inverseBasis,prize)
    newCoefficients = np.array([round(coefficients[0]),round(coefficients[1])])


    # if math.isclose(coefficients[0],round(coefficients[0]),abs_tol=1e-09)\
    #       and math.isclose(coefficients[1],round(coefficients[1]),abs_tol=1e-09):
    #     total += 3*round(coefficients[0]) + round(coefficients[1])

    # Better way than checking if its an int is to double check it works when rounded:
    if (np.matmul(basis, newCoefficients) == prize).all():
        total += 3*newCoefficients[0] + newCoefficients[1]
    
    
    # Part 1
    # times = 100
    # for j in range(times+1):
    #     vectorSum = prize - (j * vectorA)
    #     # print(vectorSum, j, vectorSum[0] / vectorB[0], vectorSum[1] / vectorB[1])
    #     if Multiples(vectorSum,vectorB) and vectorSum[0] / vectorB[0] <= 100:
    #         # print(vectorSum[0] / vectorB[0])
    #         total += 3*j + vectorSum[0] / vectorB[0]
    #         break

print(int(total))