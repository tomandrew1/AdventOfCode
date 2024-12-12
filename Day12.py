file = open("Day12-Input.txt","r")
data = file.read()

# Simple case:
data = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

rows = data.split("\n")
# columns = []
# for i in range(len(rows[0])):
#     columns.append("".join([x[i] for x in rows]))

# Idea - 
# Area is number of the type of plot to appear
# Perimeter is sum of the lengths of the rectangle that the plot spans + any interior perimeter from interior plots

# Maybe this means I need to separate regions into their own map, this will reuqire a lot of computation
# 

# Brute force




class Plot():
    def __init__(self):
        self._area = 0
        self._perimeter = 0

    def getArea(self):
        return self._area
    def getPerimeter(self):
        return self._perimeter

    def addArea(self,val):
        self._area += val
    def addPerimeter(self,val):
        self._perimeter += val

    def addPoint(self,point):
        seenPlots[point] = self
    
class Coords:
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y 
    
    def getX(self):
        return self.X
    def getY(self):
        return self.Y
    
def CreateSubplot(coord):
    seenPlots[coord].addArea(1)
    X = coord.getX()
    Y = coord.getY()
    perimeter = 4
    if X > 0 and rows[X-1][Y] == plotType:
        newCoord = Coords(X-1,Y)
        seenPlots[coord].addPoint(newCoord)
        CreateSubplot(newCoord)
        perimeter -= 1
    if X < len(rows)-1 and rows[X+1][Y] == plotType:
        newCoord = Coords(X+1,Y)
        seenPlots[coord].addPoint(newCoord)
        CreateSubplot(newCoord)
        perimeter -= 1
    if Y > 0 and rows[X][Y-1] == plotType:
        newCoord = Coords(X,Y-1)
        seenPlots[coord].addPoint(newCoord)
        CreateSubplot(newCoord)
        perimeter -= 1
    if Y < len(rows[0])-1 and rows[X][Y+1] == plotType:
        newCoord = Coords(X,Y+1)
        seenPlots[coord].addPoint(newCoord)
        CreateSubplot(newCoord)
        perimeter -= 1
    seenPlots[coord].addPerimeter(perimeter)
    

# Create all the plots and points each index to their given plot in a dictionary

# Dictionary Coords(i,j) : Plot()
seenPlots = {}
for i, row in enumerate(rows):
    for j, col in enumerate(rows[0]):
        plotType = row[j]
        coord = Coords(i, j)
        if coord not in seenPlots:
            seenPlots[coord] = Plot()
            CreateSubplot(coord)

# Get all the plots from the dictionary into a set
plotList = set()
for coords in seenPlots:
    plotList.add(seenPlots[i])

# Sum up each plots area * perimeter for the set of plots
total = 0
for plot in plotList:
    total += plot.getArea() * plot.getPerimeter()

print(total)