
import numpy as np

class Seat:
    def __init__(self, row, column, ID):
        self.row = row
        self.column = column
        self.ID = ID

    def __str__(self):
        return "row {}, column {}, seat ID {}".format(self.row, self.column, self.ID)



def decode(line):
    rl = 0
    rh = 127
    cl = 0
    ch = 7
    for c in line[:7]:
        if c == "F":
            rh -= int((rh - rl + 1) / 2)
        elif c == "B":
            rl += int((rh - rl + 1) / 2)
    for c in line[7:]:
        if c == "L":
            ch -= int((ch - cl + 1) / 2)
        elif c == "R":
            cl += int((ch - cl + 1) / 2)
    return Seat(rl, cl, rl * 8 + cl)



def read_data(filename):
    with open(filename, "r") as fh:
        lines = fh.read().splitlines()
    return lines

def get_seats(data):
    seats = []
    for line in data:
        seats.append(decode(line))
    return seats

def get_seatIDs(data):
    seatIDs = []
    for line in data:
        seatIDs.append(decode(line).ID)
    return seatIDs

def part_one(data):
    seats = get_seats(data)
    highestSeatID = 0
    for seat in seats:
        if seat.ID > highestSeatID:
            highestSeatID = seat.ID
    print("Part 1: ", highestSeatID)

def part_two(data):
    seatIDs = get_seatIDs(data)
    seatIDs.sort()
    mySeat = 0
    for i in range(len(seatIDs)):
        if seatIDs[i + 1] - seatIDs[i] > 1:
            mySeat = seatIDs[i] + 1
            break
    print("Part 2: ", mySeat)
            

def main():
    data = read_data("data")
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    main()
