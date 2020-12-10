

def read_data(filename):
    with open(filename, "r") as fh:
        lines = fh.read().splitlines()
    data = []
    for number in lines:
        data.append(int(number))
    return data


def find_anomaly(data, preambleLength = 25):
    for i in range(preambleLength, len(data)):
        previous = data[i - preambleLength: i]
        if not sum_exists(previous, data[i]):
            return data[i]


def sum_exists(previous, number):
    previous.sort()
    l = 0
    h = len(previous) - 1
    while l < h:
        s = previous[l] + previous[h]
        if s == number:
            return True
        elif s < number:
            l += 1
        elif s > number:
            h -= 1
    return False


def find_numbers(data, anomaly):
    l = 0
    h = 1
    s = 0
    while s != anomaly:
        s = sum(data[l:h])
        if s < anomaly:
            h += 1
        elif s > anomaly:
            l += 1
    return data[l:h]


def part_one(data):
    anomaly = find_anomaly(data)
    print("Part 1: ", anomaly)


def part_two(data):
    anomaly = find_anomaly(data)
    numbers = find_numbers(data, anomaly)
    print("Part 2: ", numbers, min(numbers) + max(numbers))


def main():
    data = read_data("data")
    part_one(data)
    part_two(data)

main()
