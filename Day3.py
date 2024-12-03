file = open("Day3-Input.txt","r")
memory = file.read()

# # Simple case:
# memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

# # Simple case part 2:
# memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


# Part 2:
doSplit = memory.split("do")

enabledList = []
enabled = True
for i in doSplit:
    if i[0:5] == "n't()":
        enabled = False
    elif i[0:2] == "()" or enabled == True:
        enabled = True
        enabledList.append(i)

memory = "".join(enabledList)

# Part 1:
memory = memory.split("mul(")

total = 0
for mults in memory:
    mults = mults[:8]
    count = 0
    while count < len(mults) and mults[count] != ")":
        count += 1
    if count < len(mults):
        mults = mults[:count]
        if len(mults) > 0:
            if "," in mults:
                
                try:
                    multsList = [int(x) for x in mults.split(",")]
                    if multsList[0] >= 0 and multsList[0] < 1000:
                        if multsList[1] >= 0 and multsList[1] < 1000:
                            total += multsList[0] * multsList[1]
                except:
                    pass

print(total)