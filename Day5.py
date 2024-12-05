file = open("Day5-Input.txt","r")
inp = file.read()

# # For simpler state
# inp = """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13
# ///
# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47"""

inp = inp.split("\n///\n")
rules = inp[0]
rules = rules.split("\n")
updates = [x.split(",") for x in inp[1].split("\n")]

# IDEA:
# Dictionary the rules in reveerse
# Scan through each update and check whether each rule is followed in the update
# This will be O(n + m*(k^2)) for n=items in rules, m=items in updates, k=items per update

# Make dictionary of rules (reversed)
rulesDict = {}
for i in rules:
    temp = i.split("|")
    if temp[1] not in rulesDict:
        rulesDict[temp[1]] = [temp[0]]
    else:
        rulesDict[temp[1]].append(temp[0])

# Check each update follows the rules
def CheckUpdates(rows):
    for i, items in enumerate(rows):
        for laterItems in range(i,len(rows)):
            try:
                if rows[laterItems] in rulesDict[items]:
                    return 0
            except:
                pass
    return 1

# Create list of valid updates (and invalid for part 2)
validUpdates = []
invalidUpdates = []
for rows in updates:
    if CheckUpdates(rows) == 1:
        validUpdates.append(rows)
    else:
        invalidUpdates.append(rows)

# Sum middle items of valid updates:
total = 0
for rows in validUpdates:
    total += int(rows[len(rows)//2])
print(total)


def OrderUpdates(rows):
    newRows = []
    for newItem in rows:
        i = len(newRows)-1
        while i >= 0:
            if newRows[i] in rulesDict.get(newItem,[]):
                newRows.insert(i+1,newItem)
                i = -1
            i-=1
        if newItem not in newRows:
            newRows.insert(0,newItem)
    return newRows

# Order invalid updates
orderedUpdates = []
for rows in invalidUpdates:
    orderedUpdates.append(OrderUpdates(rows))

# Sum middle items of ordered updates:
total = 0
for rows in orderedUpdates:
    total += int(rows[len(rows)//2])
print(total)