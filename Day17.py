from time import time
start = time()

file = open("Day17-Input.txt","r")
data = file.read()

# # Simple case part 1:
# data = """Register A: 729
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0"""

# # Simple case part 2:
# data = """Register A: 2024
# Register B: 0
# Register C: 0

# Program: 0,3,5,4,3,0"""

data = data.splitlines()
regA = int(data[0].split(": ")[1])
regB = int(data[1].split(": ")[1])
regC = int(data[2].split(": ")[1])
program = [int(x) for x in data[4].split(": ")[1].split(",")]

print(regA,regB,regC,program,sep="\n")

class Registers:
    def __init__(self, regA, regB, regC):
        self.regA = regA
        self.regB = regB
        self.regC = regC
        self.output = []
        self.instructionPointer = 0

    def Combo(self, operand):
        comboOperand = {
            0: operand,
            1: operand,
            2: operand,
            3: operand,
            4: self.regA,
            5: self.regB,
            6: self.regC,
            7: None,
        }
        return comboOperand[operand]
    
    def adv(self, operand):
        self.regA = self.regA//(2**self.Combo(operand))
    def bxl(self, operand):
        self.regB = self.regB ^ operand
    def bst(self, operand):
        self.regB = self.Combo(operand)%8
    def jnz(self, operand):
        if self.regA != 0:
            self.instructionPointer = operand - 2 # -2 in order to account for the +2 jump after each instruction
    def bxc(self, operand):
        self.regB = self.regB ^ self.regC
    def out(self, operand):
        self.output.append(self.Combo(operand)%8) # need to append as string for part 1
    def bdv(self, operand):
        self.regB = self.regA//(2**self.Combo(operand))
    def cdv(self, operand):
        self.regC = self.regA//(2**self.Combo(operand))

    def Opcode(self, opcode, operand):
        operations = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }

        operations[opcode](operand)

    # Run with regA as A for part 1, variableA for part 2:
    def Run(self):
        while self.instructionPointer < len(program)-1:
            
            self.Opcode(program[self.instructionPointer],program[self.instructionPointer+1])
            self.instructionPointer += 2

            # print(self.output, variableA)

            # if len(self.output) > 0 and self.output[-1] != program[len(self.output)-1]:
            #     return []
            
        # print(",".join(output))
        return self.output

A = regA
B = regB
C = regC

temp = int(0o1000000000000000) # as output will have same digits as number in octal
temp = 190384615275008 # figured out through incrementing through large octal numbers (close to first 4 digits of output)

variableA = temp 
equivProgram = []
pointer = len(program)-1
count = 0
while equivProgram != program:
    registers = Registers(int(variableA), B, C)

    equivProgram = registers.Run()
    print("a:", variableA, "oct(a):", oct(int(variableA)), "output:", registers.output) # helps debugging and searching

    # # To increment through large octal numbers to know where to start searching from optimally
    # if equivProgram[pointer] != program[pointer] and count < 7:
    #     variableA += temp
    #     count += 1
    # else:
    #     count = 0
    #     temp = temp / 8
    #     variableA += temp
    #     pointer -= 1

    variableA += 1 # for incrementing slowly for the last part of the solution


print(variableA-1)

end = time()
print(end-start)