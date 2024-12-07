file = open("Day7-Input.txt","r")
inp = file.read()

# inp = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20"""

inp = [[y.strip().split(" ") for y in x.split(":")] for x in inp.split("\n")]
for i in range(len(inp)):
    inp[i][1] = [int(x) for x in inp[i][1]]

def CheckLine(goal,nums,runningTotal):
    if len(nums) == 0:
        return runningTotal == goal

    addTotal = runningTotal + nums[0]
    multTotal = max(runningTotal,1) * nums[0]
    
    # Part 2 addition:
    concatBool = False
    concatBool = CheckLine(goal,nums[1:],int(str(runningTotal)+str(nums[0])))
    # (part 2 end) 

    
    addBool = False
    multBool = False
    if addTotal <= goal:
        addBool = CheckLine(goal,nums[1:],addTotal)
    if multTotal <= goal:
        multBool = CheckLine(goal,nums[1:],multTotal)

    return (addBool or multBool or concatBool) # changed for part 2

total = 0
for lines in inp:
    goal = int(lines[0][0])
    nums = lines[1]
    total += goal * CheckLine(goal,nums,0)
        
print(total)
