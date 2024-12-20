import numpy as np

file = open("Day16-Input.txt","r")
data = file.read()

# # Simple case:
# data = """###############
# #.......#....E#
# #.#.###.#.###.#
# #.....#.#...#.#
# #.###.#####.#.#
# #.#.#.......#.#
# #.#.#####.###.#
# #...........#.#
# ###.#.#####.#.#
# #...#.....#.#.#
# #.#.#.###.#.#.#
# #.....#...#.#.#
# #.###.#.#.#.#.#
# #S..#.....#...#
# ###############"""

# # Second example:
# data = """#################
# #...#...#...#..E#
# #.#.#.#.#.#.#.#.#
# #.#.#.#...#...#.#
# #.#.#.#.###.#.#.#
# #...#.#.#.....#.#
# #.#.#.#.#.#####.#
# #.#...#.#.#.....#
# #.#.#####.#.###.#
# #.#.#.......#...#
# #.#.###.#####.###
# #.#.#...#.....#.#
# #.#.#.#####.###.#
# #.#.#.........#.#
# #.#.#.#########.#
# #S#.............#
# #################"""

# # Third?:
# data = """##########
# #.......E#
# #.##.#####
# #..#.....#
# ##.#####.#
# #S.......#
# ##########"""

mapData = [[y for y in x] for x in data.split("\n")]

# Idea is to convert this 2D array into a graph of nodes and implement a dijkstra-like algorithm

# Class for nodes, contains their min weight for algorithm and their adj nodes
class Node():
    def __init__(self, pointers, coords): # dir = [N, E, S, W]
        self._pointers = pointers
        self._coords = coords
        self._weight = float("inf")

    def getCoords(self):
        return self._coords

    def setDir(self,dir):
        self._dir = dir

    def setMinWeight(self, val):
        if val <= self._weight:
            self._weight = val
            return True
        return False
    def getWeight(self):
        return self._weight

    def considerNewWeights(self, dir, currentWeight):
        # dir = self._dir
        for i, nodes in enumerate(self._pointers):
            # Checks node hasn't been visited yet
            if nodes == None or i in visited.get(nodes,[]):
                continue
            
            if i == dir:
                newWeight = 1
            elif abs(i-dir) == 2:
                newWeight = 2001
            else:
                newWeight = 1001
            # nodes.setMinWeight(self._weight + newWeight)
            # if change:
            #     potentialDict[nodes] = nodes.getWeight()
            #     nodes.setDir(i)
            heapq.heappush(priority_queue, (currentWeight + newWeight, nodes, i))

    # Fix pointer issue, ie change pointer coords to nodes:
    def fixPointers(self):
        for i, coords in enumerate(self._pointers):
            if coords in graphNodes:
                self._pointers[i] = graphNodes[coords]
            else:
                self._pointers[i] = None

    # Add comparison method for heapq
    def __lt__(self, other):
        return self.getWeight() < other.getWeight() 
        

# Create a dictionary of coords -> nodes (pointer in nodes are coords)
graphNodes = {}
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
        elif items == "S":
            graphNodes[coords] = temp
            start = coords
        elif items == "E":
            graphNodes[coords] = temp
            end = coords

# Fixing pointers to point directly to nodes for ease of use
for coords in graphNodes:
    graphNodes[coords].fixPointers()

root = graphNodes[start]

# # dir is NESW so dir+1%4 is rotation 90 clockwise
# root.setDir(1) # East initially
# root.setMinWeight(0) # no weight for start node

import heapq
priority_queue = []
heapq.heappush(priority_queue, (0, root, 1))  # Start root node with direction 1, ie east

potentialDict = {}
currentNode = root # to allow the entering of the while loop
visited = {}
while currentNode.getCoords() != end:
    currentWeight, currentNode, currentDir = heapq.heappop(priority_queue)

    print("COORDS:", currentNode.getCoords(), "WEIGHT:", currentWeight)

    visited.setdefault(currentNode, []).append(currentDir)
    currentNode.considerNewWeights(currentDir, currentWeight)

    # # Find smallest value in potentialDict and set current to first key that has this value
    # smallest = min(potentialDict.values())
    # temp = [key for key in potentialDict if potentialDict[key] == smallest]
    # current = temp[0]
    # potentialDict.pop(current)

    
print(currentWeight)



# # Recurrsive function to build the graph
# seen = {}
# def recurr(coords):
#     # Base case for if already visited or non-existent:
#     if coords in seen:
#         return seen[coords]
#     elif coords not in graphNodes:
#         return None
    
#     cardinals = [tuple(np.add(coords,(-1,0))),
#                  tuple(np.add(coords,(0,1))),
#                  tuple(np.add(coords,(1,0))),
#                  tuple(np.add(coords,(0,-1)))]
#     seen[coords] = Node([recurr(cardinals[0]),
#                  recurr(cardinals[1]),
#                  recurr(cardinals[2]),
#                  recurr(cardinals[3])], coords)
#     return seen[coords]
# # Root node of the graph
# root = recurr(start)





# import heapq

# # dir is NESW so dir+1%4 is rotation 90 clockwise
# root.setDir(1) # East initially
# root.setMinWeight(0) # no weight for start node

# # Priority queue for nodes: (weight, node)
# priority_queue = []
# heapq.heappush(priority_queue, (0, root))  # Start node with weight 0

# visited = set()

# while priority_queue:
#     current_weight, current_node = heapq.heappop(priority_queue)

    

#     if current_node.getCoords() == end:
#         print(current_weight)
#         break

#     current_node.considerNewWeights()
#     for neighbor in current_node._pointers:
#         if neighbor and neighbor.getCoords() not in visited:
#             heapq.heappush(priority_queue, (neighbor.getWeight(), neighbor))
