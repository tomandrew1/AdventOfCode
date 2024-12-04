file = open("Day4-Input.txt","r")
a = [lines.strip() for lines in file]

# # For simple case
# file = """MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX"""
# a = [x.strip() for x in file.split("\n")]

# Part 1
def CheckDiagonals(a,i,j):
    total = 0
    if i < len(a[j])-3:
        temp = a[i+1][j] + a[i+2][j] + a[i+3][j]
        if temp == "MAS":
            total += 1
        if j < len(a)-3:
            temp = a[i+1][j+1] + a[i+2][j+2] + a[i+3][j+3]
            if temp == "MAS":
                total += 1
    if i > 2:
        temp = a[i-1][j] + a[i-2][j] + a[i-3][j]
        if temp == "MAS":
            total += 1
        if j > 2:
            temp = a[i-1][j-1] + a[i-2][j-2] + a[i-3][j-3]
            if temp == "MAS":
                total += 1
    if j < len(a)-3:
        temp = a[i][j+1] + a[i][j+2] + a[i][j+3]
        if temp == "MAS":
            total += 1
        if i > 2:
            temp = a[i-1][j+1] + a[i-2][j+2] + a[i-3][j+3]
            if temp == "MAS":
                total += 1
    if j > 2:
        temp = a[i][j-1] + a[i][j-2] + a[i][j-3]
        if temp == "MAS":
            total += 1
        if i < len(a[j])-3:
            temp = a[i+1][j-1] + a[i+2][j-2] + a[i+3][j-3]
            if temp == "MAS":
                total += 1

    return total

total = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == "X":
            total += CheckDiagonals(a,i,j)

print(total)


# Part 2
def CheckX(a,i,j):
    if a[i-1][j-1] == "M" and a[i+1][j+1] == "S":
        if a[i+1][j-1] == "M" and a[i-1][j+1] == "S":
            return 1
        elif a[i+1][j-1] == "S" and a[i-1][j+1] == "M":
            return 1
    elif a[i-1][j-1] == "S" and a[i+1][j+1] == "M":
        if a[i+1][j-1] == "M" and a[i-1][j+1] == "S":
            return 1
        elif a[i+1][j-1] == "S" and a[i-1][j+1] == "M":
            return 1
    return 0

total = 0
for i in range(1,len(a)-1):
    for j in range(1,len(a[i])-1):
        if a[i][j] == "A":
            total += CheckX(a,i,j)
print(total)