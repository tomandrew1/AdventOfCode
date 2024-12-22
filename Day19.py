file = open("Day19-Input.txt","r")
data = file.read()

# data = """r, wr, b, g, bwu, rb, gb, br

# brwrr
# bggr
# gbbr
# rrbgbr
# ubwu
# bwurrg
# brgr
# bbrgwb"""

data = data.split("\n")

patterns = [x.strip() for x in data[0].split(",")]
designs = list(data[2:])

def recurr(design):
    if len(design) == 0:
        return True
    for pattern in patterns:
        if pattern == design[:len(pattern)]:
            if recurr(design[len(pattern):]):
                return True
    return False

# Part 2:
seen = {}
def recurr2(design):
    total = 0
    if len(design) == 0:
        return 1
    for pattern in patterns:
        if pattern == design[:len(pattern)]:
            if design[len(pattern):] not in seen:
                seen[design[len(pattern):]] = recurr2(design[len(pattern):])
            total += seen[design[len(pattern):]]
    return total

total = 0
for i, design in enumerate(designs):
    total += recurr2(design)

print(total)