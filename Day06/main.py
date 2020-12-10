

def read_data(filename):
    with open(filename, "r") as fh:
        lines = fh.read().splitlines()
    return lines


def parse_group(group):
    answeredQuestions = []
    for person in group:
        for c in person:
            if c not in answeredQuestions:
                answeredQuestions.append(c)
    return answeredQuestions

def parse_group_two(group):
    answeredQuestionsByAll = group[0]
    for person in group:
        toBeRemoved = ""
        for c in answeredQuestionsByAll:
            if c not in person:
                toBeRemoved += c
        for c in toBeRemoved:
            answeredQuestionsByAll = answeredQuestionsByAll.replace(c, "")
    return answeredQuestionsByAll


def part_one(data):
    noOfYes = 0
    group = []
    for line in data:
        if line == "":
            noOfYes += len(parse_group(group))
            group = []
        else:
            group.append(line)
    print("Part 1: ", noOfYes)

def part_two(data):
    noOfYesByAll = 0
    group = []
    for line in data:
        if line == "":
            noOfYesByAll += len(parse_group_two(group))
            group = []
        else:
            group.append(line)
    print("Part 2: ", noOfYesByAll)



def main():
    data = read_data("data")
    data.append("")
    part_one(data)
    part_two(data)


main()
