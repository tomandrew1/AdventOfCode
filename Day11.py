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

# class Chain:
#     def __init__(self,val):
#         self._val = val


# Part 1:
def CheckAppearance():
    pass

def NewBlink(data):
    newData = []

    for dataVal in data:
        if dataVal in store:
            for items in store[dataVal]:
                if items in appearances:
                    appearances[items] += 1
                else:
                    newData.append(items)
                    appearances[items] = 1
        elif len(str(dataVal))%2 == 0:
            temp1,temp2 = int( str(dataVal)[:len(str(dataVal))//2]),int( str(dataVal)[len(str(dataVal))//2:])
            if temp1 in appearances:
                pass
            newData.append(temp1)
            newData.append(temp2)
            store[dataVal] = (temp1,temp2)
        else:
            temp = dataVal*2024
            newData.append(temp)
            store[dataVal] = (temp,)
    return newData

appearances = {}

for i in range(75):
    data = NewBlink(data)
    print(i,"/75")

print(len(data))