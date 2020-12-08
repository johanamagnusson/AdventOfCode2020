import numpy as np

def read_data(filename):
    with open(filename, "r") as fh:
        lines = fh.read().splitlines()
    return lines


def traverse(right, down, currentPos):
    currentPos[0] += down
    currentPos[1] += right

def test_slope(right, down, data):
    if len(data) % down != 0:
        del data[-1]
    currentPos = [0, 0]
    noOfTrees = 0
    rowLength = len(data[0])
    for i in range(int(len(data) / down)):
        if data[currentPos[0]][currentPos[1] % rowLength] == "#":
            noOfTrees += 1
        traverse(right, down, currentPos)
    return noOfTrees

def part_one(data):
    noOfTrees = test_slope(3, 1, data)
    print("Part 1: ", noOfTrees)

def part_two(data):
    noOfTreesList = []
    noOfTreesList.append(test_slope(1, 1, data))
    noOfTreesList.append(test_slope(3, 1, data))
    noOfTreesList.append(test_slope(5, 1, data))
    noOfTreesList.append(test_slope(7, 1, data))
    noOfTreesList.append(test_slope(1, 2, data))
    prod = 1
    for x in noOfTreesList:
        prod *= x
    print("Part 2: ", noOfTreesList, prod)
        

def main():
    data = read_data("data")
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    main()
