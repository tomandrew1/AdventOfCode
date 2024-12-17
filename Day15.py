import numpy as np

file = open("Day15-Input.txt","r")
data = file.read()

# # Simple case:
# data = """########
# #..O.O.#
# ##@.O..#
# #...O..#
# #.#.O..#
# #...O..#
# #......#
# ########

# <^^>>>vv<v>>v<<"""

# # Simple case part 2:
# data = """#######
# #...#.#
# #.....#
# #..OO@#
# #..O..#
# #.....#
# #######

# <vv<<^^<<^^"""


# # Medium case:
# data = """##########
# #..O..O.O#
# #......O.#
# #.OO..O.O#
# #..O@..O.#
# #O#..O...#
# #O..O..O.#
# #.OO.O.OO#
# #....O...#
# ##########

# <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
# vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
# ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
# <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
# ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
# ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
# >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
# <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
# ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
# v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

data = data.split("\n\n")
mapData = [[y for y in x] for x in data[0].split("\n")]
instructions = data[1].replace("\n","")

# print(*mapData,sep="\n")

def findRobot():
    for i, rows in enumerate(mapData):
        for j, items in enumerate(rows):
            if items == "@":
                return np.array([i, j])
coords = findRobot()

# directions as ^v<>
directions = {"^": np.array([-1,0]),
              "v": np.array([1,0]),
              "<": np.array([0,-1]),
              ">": np.array([0,1])}

# def Ray(dir):
#     nextPoint = coords
#     while True:
#         nextPoint = nextPoint + dir
#         nextVal = mapData[nextPoint[0]][nextPoint[1]]
#         if nextVal == "#":
#             return False
#         if nextVal == ".":
#             return nextPoint

# def Push(dir, target):
#     while not((target == coords).all()):
#         nextPoint = target - dir
#         mapData[target[0]][target[1]] = mapData[nextPoint[0]][nextPoint[1]]
#         target = nextPoint
#     mapData[target[0]][target[1]] = "."
    
# Part 1:
# for moves in instructions:
#     dir = directions[moves]
#     nextFree = Ray(dir)
#     if type(nextFree) == bool:
#         continue
#     else:
#         Push(dir,nextFree)
#         coords = coords + dir

# print(*mapData,sep="\n")

# total = 0
# for i, rows in enumerate(mapData):
#         for j, items in enumerate(rows):
#             if items == "O":
#                 total += 100*i + j
# print(total)





# Part 2:
# Idea is to change everything and reprogram ray and pull functions:

# Change sizes of everything:
mapData = [[y for y in x] for x in data[0].split("\n")]
i = 0
while i < len(mapData):
    rows = mapData[i]
    j = 0
    while j < len(mapData[i]):
        items = rows[j]
        if items == "#":
            mapData[i].insert(j,"#")
        elif items == ".":
            mapData[i].insert(j,".")
        elif items == "O":
            mapData[i].insert(j,"[")
            mapData[i][j+1] = "]"
        else:
            mapData[i].insert(j,"@")
            mapData[i][j+1] = "."
        j += 2
    i += 1
# print(*mapData,sep="\n")
coords = findRobot()

def Ray(moves, coords):
    dir = directions[moves]
    nextPoint = coords
    while True:
        nextPoint = nextPoint + dir
        nextVal = mapData[nextPoint[0]][nextPoint[1]]
        if nextVal == "#":
            return False
        if nextVal == ".":
            return True
        if nextVal == "[" and (moves == "^" or moves == "v"):
            nextPointAdj = nextPoint + np.array([0,1])
            if not Ray(moves,nextPointAdj):
                return False
        elif nextVal == "]" and (moves == "^" or moves == "v"):
            nextPointAdj = nextPoint + np.array([0,-1])
            if not Ray(moves,nextPointAdj):
                return False

def Push(moves, coords):
    dir = directions[moves]
    current = coords
    nextPoint = current + dir
    nextVal = mapData[nextPoint[0]][nextPoint[1]]
    # Find the empty coord
    while nextVal != ".":
        if nextVal == "[" and (moves == "^" or moves == "v"):
            nextPointAdj = nextPoint + np.array([0,1])
            Push(moves, nextPointAdj)
        elif nextVal == "]" and (moves == "^" or moves == "v"):
            nextPointAdj = nextPoint + np.array([0,-1])
            Push(moves, nextPointAdj)

        nextPoint = nextPoint + dir
        nextVal = mapData[nextPoint[0]][nextPoint[1]]
        
    # Reverse back to origin:
    current = nextPoint
    while not(current==coords).all():
        nextPoint = current - dir
        mapData[current[0]][current[1]] = mapData[nextPoint[0]][nextPoint[1]]
        current = nextPoint
    mapData[current[0]][current[1]] = "."
    # print(*mapData,sep="\n")
    # print()

for moves in instructions:
    dir = directions[moves]
    if Ray(moves, coords):
         Push(moves, coords)
         coords = coords + dir
        
# print(*mapData,sep="\n")

total = 0
for i, rows in enumerate(mapData):
        for j, items in enumerate(rows):
            if items == "[":
                total += 100*i + j
print(total)