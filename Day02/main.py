

class DataLine:
    def __init__(self, policyMin, policyMax, letter, password):
        self.policyMin = policyMin
        self.policyMax = policyMax
        self.letter = letter
        self.password = password

    def __str__(self):
        return "{}-{} {}: {}".format(self.policyMin, self.policyMax, self.letter, self.password)


def read_data(filename):
    with open(filename, "r") as fh:
        lines = fh.readlines()
    data = []
    for line in lines:
        tmp = line.split(" ")[0].split("-")
        policyMin = int(tmp[0])
        policyMax = int(tmp[1])
        tmp = line.split(" ")[1]
        letter = tmp[0]
        tmp = line.split(" ")[2]
        password = tmp.replace("\n","")
        data.append(DataLine(policyMin, policyMax, letter, password))
    return data




def part_one(data):
    noOfValidPws = 0
    for line in data:
        letterCount = line.password.count(line.letter)
        if letterCount >= line.policyMin and letterCount <= line.policyMax:
            noOfValidPws += 1
    print("Part 1: ", noOfValidPws)


def part_two(data):
    noOfValidPws = 0
    for line in data:
        if line.password[line.policyMin - 1] == line.letter:
            if line.password[line.policyMax - 1] != line.letter:
                noOfValidPws += 1
        elif line.password[line.policyMax - 1] == line.letter:
            noOfValidPws += 1
    print("Part 2: ", noOfValidPws)


def main():
    data = read_data("data")
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    main()
