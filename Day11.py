file = open("Day11-Input.txt","r")
data = file.read()

# # Simpler case:
# data = "125 17"

data = [int(x) for x in data.split(" ")]

# Part 1:
def Blink():
    index = 0
    while index < len(data):
        dataVal = data[index]
        if dataVal in store:
            data[index] = store[dataVal][0]
            if len(store[dataVal]) == 2:
                data.insert(index+1,store[dataVal][1])
                index += 1
        # elif dataVal == "0":
        #     data[index] = "1"
        #     store[dataVal] = data[index]
        elif len(dataVal)%2 == 0:
            temp1,temp2 = dataVal[:len(dataVal)//2],str(int(dataVal[len(dataVal)//2:]))
            data[index] = temp1
            data.insert(index+1,temp2)
            store[dataVal] = [temp1,temp2]
            index += 1
        else:
            data[index] = str(int(data[index])*2024)
            store[dataVal] = [data[index]]
            
        index += 1
        
# for i in range(25):
#     Blink()

# print(len(data))

# Part 2:

# Idea - dynamic programming, ie find the list of stones created when a given number is calculated
# Then store this for each instance of numbers seen to remove repeated computations 
# This means I am going to modify my brute force from part 1
store = {0:[1]} # start with 0 to remove one of the if statements in blink
# This doesn't cut down the computation enough!!

# instead keep the data as a dict with the number of times the key has appeared and iterate that:
# (still using the store dictionary to speed things up too)
def NewBlink():
    newData = {}
    for dataKey in dataDict:
        if dataKey in store:
            for items in store[dataKey]:
                newData[items] = newData.get(items,0) + dataDict.get(dataKey,0)
        elif len(str(dataKey))%2 == 0:
            temp1,temp2 = int( str(dataKey)[:len(str(dataKey))//2]),int( str(dataKey)[len(str(dataKey))//2:])
            newData[temp1] = newData.get(temp1,0) + dataDict.get(dataKey,0)
            newData[temp2] = newData.get(temp2,0) + dataDict.get(dataKey,0)
            store[dataKey] = (temp1,temp2)
        else:
            temp = dataKey*2024
            newData[temp] = newData.get(temp,0) + dataDict.get(dataKey,0)
            store[dataKey] = (temp,)
    return newData

dataDict = {}
for i in data:
    dataDict[i] = dataDict.get(i,0) + 1

for i in range(75):
    dataDict = NewBlink()
    print(i+1,"/75") # to see the speed of alogrithm

total = 0
for i in dataDict:
    total += dataDict[i]
print(total)