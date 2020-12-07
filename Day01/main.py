
import math


def read_data(filename):
    with open(filename, "r") as fh:
        lines = fh.readlines()
    data = []
    for line in lines:
        data.append(int(line))
    return data

def part_one(data):
    sortedData = sorted(data)

    n = 0
    for a in sortedData:
        i = 1
        s = math.inf
        while s > 2020:
            b = sortedData[-i]
            s = a + b
            i += 1
            n += 1
        if s == 2020:
            return a, b, s, a * b, n
        


def part_two(data):
    sortedData = sorted(data)

    n = 0
    for i in range(len(sortedData)):
        for j in range(i + 1, len(sortedData)):
            a = sortedData[i]
            b = sortedData[j]
            k = 1
            s = math.inf
            while s > 2020 and k < len(sortedData) + 1:
                c = sortedData[-k]
                s = a + b + c
                k += 1
                n += 1
            if s == 2020:
                return a, b, c, s, a * b * c, n
    

def main():
    data = read_data("data")
    print("Part 1: ", part_one(data))
    print("Part 2: ", part_two(data))



if __name__ == "__main__":
    main()
