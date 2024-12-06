file = open("Day6-Input.txt","r")
inp = file.read()

# # Simple case:
# inp = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""

map = [[chars for chars in lines] for lines in inp.split("\n")]

# Find the guard (^)
for i, lines in enumerate(map):
    try:
        pointer = [i,lines.index("^")]
    except:
        pass

# Enum for cardinal directions
from enum import Enum
class Dir(Enum):
    N = 0
    E = 1
    S = 2
    W = 3


def Part1(map,pointer):
    direction = Dir.N
    repeatPoint = None
    repeatDirection = None
    # Step until exit
    while not((direction == Dir.N and pointer[0] == 0)\
        or (direction == Dir.S and pointer[0] == len(map)-1)\
        or (direction == Dir.W and pointer[1] == 0)\
        or (direction == Dir.E and pointer[1] == len(map[0])-1)):
        if direction == Dir.N:
            nextPoint = map[pointer[0]-1][pointer[1]]
            if nextPoint != "#" and nextPoint != "O":
                nextPoint = "^"
                map[pointer[0]][pointer[1]] = "X"
                pointer = [pointer[0]-1,pointer[1]]
            else:
                # For part 2
                if nextPoint == "O":
                    repeatPoint = pointer.copy()
                    repeatDirection = direction.value
                direction = Dir((direction.value + 1) % 4)
        elif direction == Dir.S:
            nextPoint = map[pointer[0]+1][pointer[1]]
            if nextPoint != "#" and nextPoint != "O":
                nextPoint = "^"
                map[pointer[0]][pointer[1]] = "X"
                pointer = [pointer[0]+1,pointer[1]]
            else:
                # For part 2
                if nextPoint == "O":
                    repeatPoint = pointer.copy()
                    repeatDirection = direction.value
                direction = Dir((direction.value + 1) % 4)
        elif direction == Dir.E:
            nextPoint = map[pointer[0]][pointer[1]+1]
            if nextPoint != "#" and nextPoint != "O":
                nextPoint = "^"
                map[pointer[0]][pointer[1]] = "X"
                pointer = [pointer[0],pointer[1]+1]
            else:
                # For part 2
                if nextPoint == "O":
                    repeatPoint = pointer.copy()
                    repeatDirection = direction.value
                direction = Dir((direction.value + 1) % 4)
        elif direction == Dir.W:
            nextPoint = map[pointer[0]][pointer[1]-1]
            if nextPoint != "#" and nextPoint != "O":
                nextPoint = "^"
                map[pointer[0]][pointer[1]] = "X"
                pointer = [pointer[0],pointer[1]-1]
            else:
                # For part 2
                if nextPoint == "O":
                    repeatPoint = pointer.copy()
                    repeatDirection = direction.value
                direction = Dir((direction.value + 1) % 4)

        if pointer == repeatPoint and repeatDirection == direction.value:
            return -1

    map[pointer[0]][pointer[1]] = "X"
    return map


# Count number of X
afterMap = Part1(map,pointer)
total = 0
for i in map:
    for j in i:
        total += j=="X" or j=="^"

print(total)

# Part 2

# No idea on how to do this so I will simply try and brute force it:
# We know it can only be placed on one of the X's as these are the ways to block its path

total = 0
for i, rows in enumerate(afterMap):
    for j, items in enumerate(rows):
        if items == "X":
            tempMap = map.copy()
            tempMap[i][j] = "O"
            if Part1(tempMap,pointer) == -1:
                total += 1
            
print(total)