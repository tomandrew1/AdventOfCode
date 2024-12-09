file = open("Day9-Input.txt","r")
inp = file.read()

# # Simple case:
# inp = "2333133121414131402"

# Part 1:

# Setting up individual blocks
blocks = []
for i,num in enumerate(inp):
    if i%2 == 0:
        for j in range(int(num)):
            blocks.append(i//2)
    else:
        for j in range(int(num)):
            blocks.append(".")

# Compacting the block
forward = 0
backward = len(blocks)-1
while forward < backward:
    if blocks[forward] != ".":
        forward += 1
    else:
        if blocks[backward] == ".":
            backward -= 1
        else:
            blocks[forward],blocks[backward] = blocks[backward],blocks[forward]
            forward += 1
            backward -= 1

# Checking sum of block
def CheckSum(blocks):
    blocks = [0 if i=="." else i for i in blocks]
    total = 0
    for i,num in enumerate(blocks):
        total += num*i
    return total
print(CheckSum(blocks))


# Least efficient part 2 ever:
# Part 2:

# Class for creating block objects that hold id and size
class Block:
    def __init__(self,index,size):
        self._index = index
        self._size = size
    
    def getIndex(self):
        return self._index
    def setIndex(self,val):
        self._index = val
    def getSize(self):
        return self._size
    def setSize(self,val):
        self._size = val


# Setting up individual blocks like part 1
blocks = []
for i,num in enumerate(inp):
    if i%2 == 0:
        for j in range(int(num)):
            blocks.append(i//2)
    else:
        for j in range(int(num)):
            blocks.append(".")

# Creating blocksList which contains size and id of each block
blocksList = []
for i,num in enumerate(inp):
    if i%2==0:
        blocksList.append(Block(i//2,int(num)))

# reverse to go through backwards
blocksList.reverse()

# Moving blocks into freespace
for temp, i in enumerate(blocksList):
    count = 0
    flag = True
    while count < len(blocks) and flag:
        if blocks[count] != ".":
            count += 1
        else:
            storeCount = count
            while count < len(blocks)-1 and blocks[count+1] == ".":
                count += 1
            freeSpaceSize = count - storeCount + 1
            if i.getSize() <= freeSpaceSize and count < blocks.index(i.getIndex()):
                blocks = ["." if x==i.getIndex() else x for x in blocks]
                blocks[storeCount:storeCount+i.getSize()] = [i.getIndex() for k in range(i.getSize())]
                flag = False
            else:
                count += 1

print(CheckSum(blocks))