file = open("Day8-Input.txt","r")
freqMap = file.read()

# # Simple case:
# freqMap = """............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............"""

freqMap = [[y for y in x] for x in freqMap.split("\n")]

# Idea is to create a list of indices for each appearance of a given frequency
# Perhaps dictionary where key=frequency, val=list of indices
# Then I can iterate through the list and find the coordinate difference between any 2 given instances
# With these I can add onto a new map both antinodes from the 2 given instances
# Finally I can count up all the unique antinodes from this new map

# In order to work with coordinates easier
class Coords:
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y 
    
    def getX(self):
        return self.X
    
    def getY(self):
        return self.Y
    

# Set up dictionary for appearances of differnet frequencies
appearances = {}
for i, rows in enumerate(freqMap):
    for j, frequencies in enumerate(rows):
        appearances.setdefault(frequencies,[]).append(Coords(i,j))
del appearances["."]

# Set up new map for the antinodes
antinodesMap = [["." for y in range(len(freqMap[0]))] for x in range(len(freqMap))]

# Add "#" to antinodesMap for each antinode that exist between 2 points
for frequencies in appearances:
    coordsList = appearances[frequencies]
    for coords1 in coordsList:
        for coords2 in coordsList:
            # # For part 1:
            # if coords1 != coords2:
            #     difference = Coords(coords1.getX()-coords2.getX(),coords1.getY()-coords2.getY())
            #     antinodesCoords = Coords(coords1.getX()+difference.getX(),coords1.getY()+difference.getY())
            #     try:
            #         if antinodesCoords.getX() >= 0 and antinodesCoords.getY() >= 0:
            #             antinodesMap[antinodesCoords.getX()][antinodesCoords.getY()] = "#"
            #     except:
            #         pass

            # Part 2 instead:
            if coords1 == coords2:
                antinodesMap[coords1.getX()][coords1.getY()] = "#"
            else:
                difference = Coords(coords1.getX()-coords2.getX(),coords1.getY()-coords2.getY())
                antinodesCoords = Coords(coords1.getX()+difference.getX(),coords1.getY()+difference.getY())
                flag = False
                while not flag and antinodesCoords.getX() >= 0 and antinodesCoords.getY() >= 0:
                    try:  
                        antinodesMap[antinodesCoords.getX()][antinodesCoords.getY()] = "#"
                        # print(*antinodesMap,sep="\n")
                        # print()
                    except:
                        flag = True
                    antinodesCoords = Coords(antinodesCoords.getX()+difference.getX(),antinodesCoords.getY()+difference.getY())

# print(*antinodesMap,sep="\n")

# Count number of antinodes:
total = 0
for rows in antinodesMap:
    for items in rows:
        total += items == "#"
print(total)