

def get_adapters(filename):
    with open(filename, "r") as fh:
        lines = fh.read().splitlines()
    adapters = [0]
    for line in lines:
        adapters.append(int(line))
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    return adapters


def cumdiff(adapters):
    diffList = []
    for i in range(1, len(adapters)):
        diffList.append(adapters[i] - adapters[i - 1])
    return diffList

def get_differences(adapters):
    differences = {1: 0, 2: 0, 3: 0}
    diffList = cumdiff(adapters)
    for diff in diffList:
        differences[diff] += 1
    return differences

def count_arrangements(index, adapters):
    global alreadyFound
    if index == len(adapters) - 1:
        return 1
    if index in alreadyFound:
        return alreadyFound[index]
    count = 0
    for i in range(index + 1, len(adapters)):
        if adapters[i] - adapters[index] <= 3:
            count += count_arrangements(i, adapters)
    alreadyFound[index] = count
    return count


def part_one(adapters):
    differences = get_differences(adapters)
    print(differences)
    print("Part 1: ", differences[1] * differences[3])

def part_two(adapters):
    count = count_arrangements(0, adapters)
    print("Part 2: ", count)


alreadyFound = {}

def main():
    adapters = get_adapters("data")
    part_one(adapters)
    part_two(adapters)

main()
