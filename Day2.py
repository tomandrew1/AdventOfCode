# import input data
file = open("Day2-Input.txt","r")
reports = file.read()

# # For simple case:
# reports = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9"""

# Convert into 2D array of integers
reports = reports.split("\n")
reports = [[int(y) for y in x.split(" ")] for x in reports]


# Function attempted to work for part 2 but only works for part 1
def CheckLevel(levels,turn):
    count = 0
    if sorted(levels) == levels or sorted(levels,reverse=True) == levels:
        while count < len(levels)-1:
            temp = abs(levels[count+1] - levels[count])
            if temp > 3 or temp == 0:
                if turn == 0:
                    ltemp = levels.copy()
                    del ltemp[count]
                    if CheckLevel(ltemp,1) == 1:
                        return 1
                    if count <= len(levels)-2:
                        ltemp = levels.copy()
                        del ltemp[count+1]
                        if CheckLevel(ltemp,1) == 1:
                            return 1
                    return 0
                else:
                    return 0
            count += 1
    else:
        if turn == 0:
            while count < len(levels):
                ltemp = levels.copy()
                del ltemp[count]
                if CheckLevel(ltemp,1) == 1:
                    return 1
                count += 1
        else:
            return 0

    return 1

# Part 1:
safe = 0
for levels in reports:
    safe += CheckLevel(levels,1)
print(safe)

# Part 2:
def CheckUnsafe(levels):
    for i in range(len(levels)):
        temp = levels.copy()
        del temp[i]
        if CheckSafe(temp):
            return 1
    return 0

def CheckSafe(levels):
    if sorted(levels) == levels or sorted(levels,reverse=True) == levels:
        count = 0
        while count < len(levels)-1:
            temp = abs(levels[count+1] - levels[count])
            if temp > 3 or temp == 0:
                return False
            count += 1
    else:
        return False
    return True


safe = 0
for levels in reports:
    if CheckSafe(levels):
        safe += 1
    else:
        safe += CheckUnsafe(levels)
print(safe)