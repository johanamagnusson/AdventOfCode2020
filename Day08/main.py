import copy



accumulator = 0

def change_acc(value):
    global accumulator
    accumulator += value

def set_acc(value):
    global accumulator
    accumulator = value

def get_instruction_list(filename):
    with open(filename, "r") as fh:
        lines = fh.read().splitlines()
    instructionList = []
    for line in lines:
        instructionList.append([line.split(" ")[0], int(line.split(" ")[1])])
    return instructionList


def execute_instruction(instruction, currentIndex):
    if instruction[0] == "nop":
        currentIndex += 1
    elif instruction[0] == "acc":
        change_acc(instruction[1])
        currentIndex += 1
    elif instruction[0] == "jmp":
        currentIndex += instruction[1]
    return currentIndex

def execute_program(instructionList, startingIndex = 0):
    currentIndex = startingIndex
    instructionsExecuted = []
    while currentIndex not in instructionsExecuted:
        instructionsExecuted.append(currentIndex)
        currentIndex = execute_instruction(instructionList[currentIndex], currentIndex)
        if currentIndex == len(instructionList):
            break
    return instructionsExecuted, currentIndex == (len(instructionList))


def part_one(instructionList):
    execute_program(instructionList)
    print("Part 1: ", accumulator)

def part_two(instructionList):
    set_acc(0)
    instructionsExecuted, success = execute_program(instructionList)
    while not success and instructionsExecuted:
        set_acc(0)
        instructionIndex = instructionsExecuted.pop(0)
        instructionListNew = copy.deepcopy(instructionList)
        if instructionList[instructionIndex][0] == "nop":
            instructionListNew[instructionIndex][0] = "jmp"
            tmp, success = execute_program(instructionListNew)
        elif instructionList[instructionIndex][0] == "jmp":
            instructionListNew[instructionIndex][0] = "nop"
            tmp, success = execute_program(instructionListNew)
    print("Part 2: ", accumulator)





def main():
    instructionList = get_instruction_list("data")
    part_one(instructionList)
    part_two(instructionList)

main()
