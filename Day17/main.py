

with open("testdata", "r") as fh:
    lines = fh.read().splitlines()

activeCubes = set()

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "#":
            activeCubes.add((i - 1, j - 1, 0, 0))


l = 15
p = 2

if p == 1:
    for _ in range(6):
        newActive = set()
        for x in range(-l, l):
            for y in range(-l, l):
                for z in range(-l, l):
                    n = 0
                    for dx in [-1,0,1]:
                        for dy in [-1,0,1]:
                            for dz in [-1,0,1]:
                                if dx != 0 or dy != 0 or dz != 0:
                                    if (x+dx, y+dy, z+dz) in activeCubes:
                                        n += 1
                    if (x,y,z) not in activeCubes and n == 3:
                        newActive.add((x,y,z))
                    if (x,y,z) in activeCubes and (n == 2 or n == 3):
                        newActive.add((x,y,z))
        activeCubes = newActive

    print("Part 1: ", len(activeCubes))

else:
    for _ in range(6):
        newActive = set()

        nbOfActive = set()
        for (x,y,z,w) in activeCubes:
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    for dz in [-1,0,1]:
                        for dw in [-1,0,1]:
                            nbOfActive.add((x+dx, y+dy, z+dz, w+dw))

        for (x,y,z,w) in nbOfActive:
            n = 0
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    for dz in [-1,0,1]:
                        for dw in [-1,0,1]:
                            if dx != 0 or dy != 0 or dz != 0 or dw != 0:
                                if (x+dx, y+dy, z+dz, w+dw) in activeCubes:
                                    n += 1
            if (x,y,z,w) not in activeCubes and n == 3:
                newActive.add((x,y,z,w))
            if (x,y,z,w) in activeCubes and (n == 2 or n == 3):
                newActive.add((x,y,z,w))
        activeCubes = newActive

    print("Part 2: ", len(activeCubes))
