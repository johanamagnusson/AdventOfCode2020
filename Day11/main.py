

with open("data", "r") as fh:
    lines = fh.read().splitlines()
layout = []
for line in lines:
    layout.append(list(line))


def adjacent(i, j):
    return [(i-1, j-1),
            (i-1, j),
            (i-1, j+1),
            (i, j-1),
            (i, j+1),
            (i+1, j-1),
            (i+1, j),
            (i+1, j+1)]

def first_visible(i, j):
    first_visible = []
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for d in directions:
        seat = [i,j]
        while True:
            seat[0] += d[0]
            seat[1] += d[1]
            if seat[0] < 0 or seat[1] < 0 or seat[0] > len(layout) - 1 or seat[1] > len(layout[i]) - 1:
                break
            elif layout[seat[0]][seat[1]] == "L" or layout[seat[0]][seat[1]] == "#":
                first_visible.append(seat)
                break
    return first_visible



noOfOccupiedSeats = 0
noOfOccupiedSeatsPrev = -1
def update_seats():
    global noOfOccupiedSeats
    global noOfOccupiedSeatsPrev
    seatsToChange = []
    noOfOccupiedSeatsPrev = noOfOccupiedSeats
    for i in range(len(layout)):
        for j in range(len(layout[i])): 
            noOccupied = 0
            if layout[i][j] == ".":
                continue
            for seat in adjacent(i,j):
                if seat[0] < 0 or seat[1] < 0 or seat[0] > len(layout) - 1 or seat[1] > len(layout[i]) - 1:
                    pass
                elif layout[seat[0]][seat[1]] == "#":
                    noOccupied += 1
            if layout[i][j] == "#" and noOccupied >= 4:
                seatsToChange.append((i,j,"L"))
                noOfOccupiedSeats -= 1
            elif layout[i][j] == "L" and noOccupied == 0:
                seatsToChange.append((i,j,"#"))
                noOfOccupiedSeats += 1
    for seat in seatsToChange:
        layout[seat[0]][seat[1]] = seat[2]

def update_seats_two():
    global noOfOccupiedSeats
    global noOfOccupiedSeatsPrev
    seatsToChange = []
    noOfOccupiedSeatsPrev = noOfOccupiedSeats
    for i in range(len(layout)):
        for j in range(len(layout[i])): 
            noOccupied = 0
            if layout[i][j] == ".":
                continue
            for seat in first_visible(i,j):
                if layout[seat[0]][seat[1]] == "#":
                    noOccupied += 1
            if layout[i][j] == "#" and noOccupied >= 5:
                seatsToChange.append((i,j,"L"))
                noOfOccupiedSeats -= 1
            elif layout[i][j] == "L" and noOccupied == 0:
                seatsToChange.append((i,j,"#"))
                noOfOccupiedSeats += 1
    for seat in seatsToChange:
        layout[seat[0]][seat[1]] = seat[2]



def print_layout():
    for row in layout:
        print("".join(row))



while noOfOccupiedSeats != noOfOccupiedSeatsPrev:
    update_seats_two()

print("Part 1: ", noOfOccupiedSeats)
