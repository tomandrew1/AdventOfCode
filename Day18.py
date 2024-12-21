import numpy as np
import heapq

file = open("Day18-Input.txt","r")


# Simple case:
data = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""
data = file.read() # override simple case

data = [(int(x.split(",")[0]),int(x.split(",")[1])) for x in data.splitlines()]

mapData = [["." for y in range(71)] for x in range(71)]
# simple case:
# mapData = [["." for y in range(7)] for x in range(7)]




# print(*mapData,sep="\n")

# Copied but simplified from day 16:

# and in order for day 16 code to work:
start = (0, 0)
end = (70,70)

# Class for nodes, contains their min weight for algorithm and their adj nodes
class Node():
    def __init__(self, pointers, coords): # dir = [N, E, S, W]
        self._pointers = pointers
        self._coords = coords
        self._weight = float("inf")

    def getCoords(self):
        return self._coords
    
    def getWeight(self):
        return self._weight

    def considerNewWeights(self):
        for i, nodes in enumerate(self._pointers):
            # Checks node hasn't been visited yet
            if nodes == None or nodes in visited:
                continue
            
            newWeight = self._weight + 1
            if newWeight < nodes.getWeight():
                nodes._weight = newWeight
                heapq.heappush(priority_queue, nodes)

    # Fix pointer issue, ie change pointer coords to nodes:
    def fixPointers(self):
        for i, coords in enumerate(self._pointers):
            if coords in graphNodes:
                self._pointers[i] = graphNodes[coords]
            else:
                self._pointers[i] = None

    # Add comparison method for heapq
    def __lt__(self, other):
        # Part 1:
        # return self.getWeight() < other.getWeight() 
        
        # Part 2, idea is to change the way heap acts in order to find a path to end faster
        return (self._coords[0] + self._coords[1]) < (other._coords[0] + other._coords[1])
        
graphNodes = {}
visited = set()
priority_queue = []
def CheckSolution():
    # Create a dictionary of coords -> nodes (pointer in nodes are coords)
    for i, rows in enumerate(mapData):
        for j, items in enumerate(rows):
            coords = (i, j)
            cardinals = [tuple(np.add(coords,(-1,0))),
                        tuple(np.add(coords,(0,1))),
                        tuple(np.add(coords,(1,0))),
                        tuple(np.add(coords,(0,-1)))]
            temp = Node([cardinals[0],
                        cardinals[1],
                        cardinals[2],
                        cardinals[3]], coords)
            if items == ".":
                graphNodes[coords] = temp

    # Fixing pointers to point directly to nodes for ease of use
    for coords in graphNodes:
        graphNodes[coords].fixPointers()
    root = graphNodes[start]
    root._weight = 0 

    heapq.heappush(priority_queue, root)

    max = float("inf") # to stay in loop until max is adjusted
    while priority_queue:
        currentNode = heapq.heappop(priority_queue)
        # print("COORDS:", currentNode.getCoords(), "WEIGHT:", currentNode.getWeight())

        visited.add(currentNode)
        currentNode.considerNewWeights()

        if currentNode.getCoords() == end:
            max = currentNode.getWeight()
    return max

# Part 1:
# for i in range(1024):
#     coords = data[i]
#     mapData[coords[0]][coords[1]] = "#"
# print(CheckSolution())

# Part 2:
i = 0
while True:
    coords = data[i]
    mapData[coords[0]][coords[1]] = "#"

    print(i)
    temp = CheckSolution()
    if temp == float("inf"):
        print(coords)
        break

    i += 1