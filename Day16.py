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

mapData = [[y for y in x] for x in data.split("\n")]

# Idea is to convert this 2D array into a graph of nodes and implement a dijkstra-like algorithm

# Create a list of needed coord nodes
graphNodes = set()
for i, rows in enumerate(mapData):
    for j, items in enumerate(rows):
        if items == "S":
            start = np.array([i, j])
        elif items == "E":
            end = np.array([i, j])
        elif items == ".":
            graphNodes.add(np.array([i, j]))

# Class for nodes, contains their min weight for algorithm and their adj nodes
class Node():
    def __init__(self, dir): # dir = [N, E, S, W]
        # self._N = dir[0]
        # self._E = dir[1]
        # self._S = dir[2]
        # self._W = dir[3]
        self._pointers = dir

    def minWeight(self, val):
        self._weight = min(val,self._weight)

    def considerNewWeights(self, coords, dir):
        for i, nodes in enumerate(self._pointers):
            if i == dir:
                newWeight = 1
            elif abs(i-dir) == 2:
                newWeight = 2001
            else:
                newWeight = 1001
            nodes.minWeight(self._weight + newWeight)

# Recurrsive function to build the graph
seen = {}
def recurr(coords):
    # Base case for if already visited or non-existent:
    if coords in seen or coords not in graphNodes:
        return None

    seen.add(coords)
    cardinals = [coords+np.array([-1,0]), 
                 coords+np.array([0,1]), 
                 coords+np.array([1,0]), 
                 coords+np.array([0,-1])]
    return Node([recurr(cardinals[0]),
                 recurr(cardinals[1]),
                 recurr(cardinals[2]),
                 recurr(cardinals[3]),])
# Root node of the graph
root = recurr(start)

# dir is NESW so dir+1%4 is rotation 90 clockwise
dir = 1 # East initially

