file = open("Day12-Input.txt","r")
data = file.read()

# # Simple case:
# data = """RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE"""

rows = data.split("\n")
# columns = []
# for i in range(len(rows[0])):
#     columns.append("".join([x[i] for x in rows]))

# Idea - 
# Area is number of the type of plot to appear
# Perimeter is sum of the lengths of the rectangle that the plot spans + any interior perimeter from interior plots

# Maybe this means I need to separate regions into their own map, this will reuqire a lot of computation



class Plot():
    def __init__(self,plotType):
        self._area = 0
        self._perimeter = 0
        self._plotType = plotType

    def getArea(self):
        return self._area
    def getPerimeter(self):
        return self._perimeter
    def getPlotType(self):
        return self._plotType

    def addArea(self,val):
        self._area += val
    def addPerimeter(self,val):
        self._perimeter += val

    def setType(self,val):
        self._type = val

    def addPoint(self,point):
        seenPlots[point] = self
    
    
def CreateSubplot(coord):
    seenPlots[coord].addArea(1)
    X = coord[0]
    Y = coord[1]
    perimeter = 4

    newCoord = (X-1,Y)
    if X > 0 and rows[X-1][Y] == seenPlots[coord].getPlotType():
        perimeter -= 1
        if newCoord not in seenPlots:
            seenPlots[coord].addPoint(newCoord)
            CreateSubplot(newCoord)
    newCoord = (X+1,Y)
    if X < len(rows)-1 and rows[X+1][Y] == seenPlots[coord].getPlotType():
        perimeter -= 1
        if newCoord not in seenPlots:
            seenPlots[coord].addPoint(newCoord)
            CreateSubplot(newCoord)
    newCoord = (X,Y-1)
    if Y > 0 and rows[X][Y-1] == seenPlots[coord].getPlotType():
        perimeter -= 1
        if newCoord not in seenPlots:
            seenPlots[coord].addPoint(newCoord)
            CreateSubplot(newCoord)
    newCoord = (X,Y+1)
    if Y < len(rows[0])-1 and rows[X][Y+1] == seenPlots[coord].getPlotType():
        perimeter -= 1
        if newCoord not in seenPlots:
            seenPlots[coord].addPoint(newCoord)
            CreateSubplot(newCoord)
    seenPlots[coord].addPerimeter(perimeter)

# Part 2
def CountSides(plots):
    coordsList = [x for x in seenPlots if seenPlots[x] == plots]

    north = [x for x in coordsList if x[0] == 0 or rows[x[0]-1][x[1]] != plots.getPlotType()]
    east = [x for x in coordsList if x[1] == len(rows[0])-1 or rows[x[0]][x[1]+1] != plots.getPlotType()]
    south = [x for x in coordsList if x[0] == len(rows)-1 or rows[x[0]+1][x[1]] != plots.getPlotType()]
    west = [x for x in coordsList if x[1] == 0 or rows[x[0]][x[1]-1] != plots.getPlotType()]

    sides = 0
    
    index = 0
    sides += len(north)
    while index < len(north):
        if (north[index][0], north[index][1]+1) in north:
            sides -= 1
        index += 1
    index = 0
    sides += len(east)
    while index < len(east):
        if (east[index][0]+1, east[index][1]) in east:
            sides -= 1
        index += 1
    index = 0
    sides += len(south)
    while index < len(south):
        if (south[index][0], south[index][1]+1) in south:
            sides -= 1
        index += 1
    index = 0
    sides += len(west)
    while index < len(west):
        if (west[index][0]+1, west[index][1]) in west:
            sides -= 1
        index += 1

    return sides
    

# Create all the plots and points each index to their given plot in a dictionary

# Dictionary (i,j) : Plot()
seenPlots = {}
for i, row in enumerate(rows):
    for j, plotType in enumerate(rows[i]):
        coord = (i, j)
        if coord not in seenPlots:
            seenPlots[coord] = Plot(plotType)
            CreateSubplot(coord)

# Get all the plots from the dictionary into a set
plotList = set()
for coords in seenPlots:
    plotList.add(seenPlots[coords])

# Sum up each plots area * perimeter for the set of plots
total = 0
for plot in plotList:
    # total += plot.getArea() * plot.getPerimeter()

    sides = CountSides(plot)
    total += plot.getArea() * sides

    # print(sides, plot.getArea(), plot.getPerimeter(), plot.getPlotType())

print(total)