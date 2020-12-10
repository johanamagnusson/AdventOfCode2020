

class Bag:
    def __init__(self, name, contains={}):
        self.name = name
        self.contains = contains
        self.isContainedIn = []

    def __str__(self):
        return "{}: {}".format(self.name, str(self.contains))


def read_and_parse(filename):
    with open(filename, "r") as fh:
        lines = fh.read().splitlines()
    bags = {}
    for line in lines:
        name = " ".join(line.split(" ")[0:2])
        contains = {}
        split = line.split(" bags contain ")
        for item in split[1].split(", "):
            if item == "no other bags.":
                break
            else:
                amount = int(item.split(" ")[0])
                contains[" ".join(item.split(" ")[1:3])] = amount
        bags[name] = Bag(name, contains)
    for bagName in bags:
        for c in bags[bagName].contains:
            if bagName not in bags[c].isContainedIn:
                bags[c].isContainedIn.append(bagName)
    return bags



def find_containing_bags(myBagName, bags):
    containingMyBag = []
    bagsList = list(bags.keys())
    bagsList.remove(myBagName)
    canHold = [myBagName]
    while canHold:
        newAdditions = []
        toBeRemoved = []
        for bagName in bagsList:
            bag = bags[bagName]
            if not bag.contains:
                toBeRemoved.append(bag.name)
                continue
            for item in canHold:
                if item in bag.contains and bag.name not in newAdditions:
                    newAdditions.append(bag.name)
                    toBeRemoved.append(bag.name)
        containingMyBag.extend(newAdditions)
        for item in toBeRemoved:
            if item in bagsList:
                bagsList.remove(item)
        canHold = newAdditions.copy()
    return containingMyBag

def find_containing_bags_non_retard(myBagName, bags):
    containingMyBag = []
    tmp = []
    tmp.extend(bags[myBagName].isContainedIn)
    while tmp:
        bagName = tmp.pop(0)
        if bagName not in containingMyBag:
            containingMyBag.append(bagName)
        tmp.extend(bags[bagName].isContainedIn)
    return containingMyBag

        


def count_bags(myBagName, bags):
    bagsToCount = [bags[myBagName]]
    multipliers = [1]
    count = 0
    while bagsToCount:
        bagToCount = bagsToCount.pop(0)
        multiplier = multipliers.pop(0)
        for bagName in bagToCount.contains:
            count += (multiplier * bagToCount.contains[bagName])
            bagsToCount.append(bags[bagName])
            multipliers.append(multiplier * bagToCount.contains[bagName])
    return count

                
def part_one(data):
    #containingMyBag = find_containing_bags("shiny gold", data)
    containingMyBag = find_containing_bags_non_retard("shiny gold", data)
    print("Part 1: ", len(containingMyBag))


def part_two(data):
    noOfBags = count_bags("shiny gold", data)
    print("Part 2: ", noOfBags)


def main():
    data = read_and_parse("data")
    part_one(data)
    part_two(data)

main()
