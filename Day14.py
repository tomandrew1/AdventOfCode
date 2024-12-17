import numpy as np

file = open("Day14-Input.txt","r")
data = file.read()
spaceDim = (103, 101)

# # Simple case:
# data = """p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
# p=3,0 v=-2,-2
# p=7,6 v=-1,-3
# p=3,0 v=-1,-2
# p=9,3 v=2,3
# p=7,3 v=-1,2
# p=2,4 v=2,-3
# p=9,5 v=-3,-3"""
# spaceDim = (7, 11)

space = np.zeros(spaceDim)


class Robots:
    def __init__(self,pos,vel):
        self._pos = pos
        self._vel = vel
    
    def getPos(self):
        return self._pos
    def getVel(self):
        return self._vel
    
    # def setPos(self,val):
    #     self._pos = val
    # def setVel(self,val):
    #     self._vel = val

    def tick(self, times, dim):
        self._pos[0] = (self._pos[0] + (times * self._vel[0])) % dim[0]
        self._pos[1] = (self._pos[1] + (times * self._vel[1])) % dim[1]

# Data formatting
data = data.split("\n")
robots = [x.replace("p=","").replace("v=","").split(" ") for x in data]
robots = [[[int(z) for z in y.split(",")[::-1]] for y in x] for x in robots] # reverse after split as x,y -> y,x in numpy arrays
robots = [Robots(x[0],x[1]) for x in robots] 


# # after 100 seconds:
# for robot in robots:
#     robot.tick(100,spaceDim)
#     # fill space with positions of robots:
#     newPos = robot.getPos()
#     space[newPos[0]][newPos[1]] += 1

print(space)

# Split into quads
quads = [space[:spaceDim[0]//2, :spaceDim[1]//2], 
         space[:spaceDim[0]//2, spaceDim[1]//2+1:],
         space[spaceDim[0]//2+1:, :spaceDim[1]//2],
         space[spaceDim[0]//2+1:, spaceDim[1]//2+1:]]

# Sum up robots in each quad and mult to total
total = 1
for quad in quads:
    total = total * np.sum(quad)
print(total)

# Part 2:


# import matplotlib.pyplot as plt
# plt.figure()
# plt.imshow(space)
# plt.show()


def tickSpace():
    space = np.zeros(spaceDim)
    for robot in robots:
        robot.tick(1,spaceDim)
        # fill space with positions of robots:
        newPos = robot.getPos()
        space[newPos[0]][newPos[1]] += 1
    return space


# connectedSpace = np.zeros((spaceDim[0]*101,spaceDim[1]))
# for i in range(64):
#     tempconnectedSpace = tickSpace()
#     for j in range(100):
#         tempconnectedSpace = np.concatenate((tempconnectedSpace,tickSpace())) 
#     print(i)
#     connectedSpace = np.concatenate((connectedSpace,tempconnectedSpace),axis=1) 
# print(connectedSpace)

from PIL import Image

# img = Image.fromarray(connectedSpace * 255)

# img.show()



concat = np.zeros(spaceDim)

for robot in robots:
    robot.tick(6377,spaceDim)
    # fill space with positions of robots:
    newPos = robot.getPos()
    space[newPos[0]][newPos[1]] += 1
# for i in range(5):
#     concat = np.concatenate((concat,tickSpace()))

img = Image.fromarray(space * 255)

img.show()
