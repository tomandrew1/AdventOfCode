file = open("Day10-Input.txt","r")
data = file.read()

# # Simple case:
# data = """89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732"""

data = [[int(y) for y in x] for x in data.split("\n")]
# dataof9 = [[0 if y==9 else "" for y in x] for x in data]

def Trail(i,j,num):
    #base case:
    if num == 9:
        return (i,j)
    mySet = set()

    if i<len(data)-1 and data[i+1][j] == num+1:
        temp = Trail(i+1,j,num+1)
        try:
            mySet.add(temp)
        except:
            mySet.update(temp)
    if i>0 and data[i-1][j] == num+1:
        temp = Trail(i-1,j,num+1)
        try:
            mySet.add(temp)
        except:
            mySet.update(temp)
    if j<len(data[0])-1 and data[i][j+1] == num+1:
        temp = Trail(i,j+1,num+1)
        try:
            mySet.add(temp)
        except:
            mySet.update(temp)
    if j>0 and data[i][j-1] == num+1:
        temp = Trail(i,j-1,num+1)
        try:
            mySet.add(temp)
        except:
            mySet.update(temp)

    return mySet

# Part 2:
def Trail2(i,j,num):
    #base case:
    if num == 9:
        return [(i,j)]
    myList = []

    if i<len(data)-1 and data[i+1][j] == num+1:
        myList += (Trail2(i+1,j,num+1))
    if i>0 and data[i-1][j] == num+1:
        myList += (Trail2(i-1,j,num+1))
    if j<len(data[0])-1 and data[i][j+1] == num+1:
        myList += (Trail2(i,j+1,num+1))
    if j>0 and data[i][j-1] == num+1:
        myList += (Trail2(i,j-1,num+1))

    return myList

# For each 0 check trails
total1 = 0
total2 = 0
for i,lines in enumerate(data):
    for j,nums in enumerate(lines):
        if nums == 0:
            total1 += len(Trail(i,j,0))
            total2 += len(Trail2(i,j,0))

print("Part 1:",total1,"\nPart 2:",total2)