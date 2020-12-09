
import re

class Passport:
    def __init__(self):
        self.byr = None 
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = None
        self.hgtUnit = None
        self.isValid = False

    def __str__(self):
        return ("byr: {}, iyr: {}, eyr: {},"
                " hgt: {}{}, hcl: {}, ecl: {}, pid: {}, cid: {}, valid: {}".format(
                    self.byr, self.iyr, self.eyr, self.hgt, self.hgtUnit, self.hcl, self.ecl,
                    self.pid, self.cid, self.isValid))


def parse_passport(passportList):
    passport = Passport()
    for item in passportList:
        split = item.split(":")
        try:
            if split[0] == "byr":
                passport.byr = int(split[1])
            elif split[0] == "iyr":
                passport.iyr = int(split[1])
            elif split[0] == "eyr":
                passport.eyr = int(split[1])
            elif split[0] == "hgt":
                passport.hgt = int(split[1].replace("cm", "").replace("in", ""))
                if "cm" in split[1]:
                    passport.hgtUnit = "cm"
                elif "in" in split[1]:
                    passport.hgtUnit = "in"
                else:
                    raise ValueError
            elif split[0] == "hcl":
                passport.hcl = split[1]
            elif split[0] == "ecl":
                passport.ecl = split[1]
            elif split[0] == "pid":
                passport.pid = split[1]
            elif split[0] == "cid":
                passport.cid = split[1]
        except ValueError:
            pass
    if len(passportList) == 8 or (len(passportList) == 7 and not passport.cid):
        passport.isValid = True
    return passport




def read_data(filename):
    with open(filename, "r") as fh:
        lines = fh.read().splitlines()
    lines.append("")
    data = []
    passportList = []
    for line in lines:
        if line == "":
            passport = parse_passport(passportList)
            data.append(passport)
            passportList = []
        else:
            for s in line.split(" "):
                passportList.append(s)
    return data


def part_one(data):
    noOfValids = 0
    for passport in data:
        if passport.isValid:
            noOfValids += 1
    print("Part 1: ", noOfValids)

def part_two(data):
    noOfValids = 0
    for passport in data:
        if passport.isValid:
            if passport.byr < 1920 or passport.byr > 2002:
                passport.isValid = False
                continue
            elif passport.iyr < 2010 or passport.iyr > 2020:
                passport.isValid = False
                continue
            elif passport.eyr < 2020 or passport.eyr > 2030:
                passport.isValid = False
                continue
            elif not re.match("^#(([0-9a-fA-F]{2}){3}|([0-9a-fA-F]){3})$", passport.hcl):
                passport.isValid = False
                continue
            elif passport.ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                passport.isValid = False
                continue
            elif not re.match("^[0-9]{9}$", passport.pid):
                passport.isValid = False
                continue

            if passport.hgtUnit == "cm":
                if passport.hgt < 150 or passport.hgt > 193:
                    passport.isValid = False
                    continue
            elif passport.hgtUnit == "in":
                if passport.hgt < 59 or passport.hgt > 76:
                    passport.isValid = False
                    continue
            else:
                passport.isValid = False
                continue
            noOfValids += 1
    for passport in data:
        if passport.isValid:
            print(passport)
    print("Part 2: ", noOfValids)





def main():
    data = read_data("data")
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    main()
