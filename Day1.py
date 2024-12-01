# Try and open file for input
file = open(".\Day1-Input.txt","r")
global inp
inp = file.read()

# Turn data into list:
inp = inp.replace("\n","   ").split("   ")

# Split list into 2 lists to represent columns
left = [inp[x] for x in range(0,len(inp),2)]
right = [inp[x] for x in range(1,len(inp),2)]

# Sort the lists
left.sort()
right.sort()


# Part 1:

# Add difference to total for each element
total = 0
for i in range(0,len(left)):
    total += abs(int(left[i])-int(right[i]))
print(total)



# Part 2:

# Set dict up for left and iterate for all left items
leftDict = {}
total = 0
for i in left:
    if not(i in leftDict):
        leftDict[i] = 0
        for j in right:
            if i == j:
                leftDict[i] = leftDict[i] + 1
        total += int(i) * leftDict[i]
    else:
        total += int(i) * leftDict[i]
print(total)