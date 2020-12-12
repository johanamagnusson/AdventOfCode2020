
import numpy as np

with open("data") as fh:
    lines = fh.read().splitlines()

instructions = []
for line in lines:
    instructions.append((line[0], int(line[1:])))

heading = np.array([1, 0])
currentPos = np.array([0, 0])

for ins in instructions:
    if ins[0] == "F":
        currentPos += (heading * ins[1])
    elif ins[0] == "N":
        currentPos[1] += ins[1]
    elif ins[0] == "S":
        currentPos[1] -= ins[1]
    elif ins[0] == "E":
        currentPos[0] += ins[1]
    elif ins[0] == "W":
        currentPos[0] -= ins[1]
    elif ins[0] == "R":
        v = -np.deg2rad(ins[1])
        R = np.array([[np.cos(v), -np.sin(v)], [np.sin(v), np.cos(v)]], int)
        heading = R.dot(heading)
    elif ins[0] == "L":
        v = np.deg2rad(ins[1])
        R = np.array([[np.cos(v), -np.sin(v)], [np.sin(v), np.cos(v)]], int)
        heading = R.dot(heading)

print("Part 1: ", currentPos, sum(abs(currentPos)))



waypoint = np.array([10, 1])
currentPos = np.array([0, 0])
for ins in instructions:
    if ins[0] == "F":
        currentPos += (waypoint * ins[1])
    elif ins[0] == "N":
        waypoint[1] += ins[1]
    elif ins[0] == "S":
        waypoint[1] -= ins[1]
    elif ins[0] == "E":
        waypoint[0] += ins[1]
    elif ins[0] == "W":
        waypoint[0] -= ins[1]
    elif ins[0] == "R":
        v = -np.deg2rad(ins[1])
        R = np.array([[np.cos(v), -np.sin(v)], [np.sin(v), np.cos(v)]], int)
        waypoint = R.dot(waypoint)
    elif ins[0] == "L":
        v = np.deg2rad(ins[1])
        R = np.array([[np.cos(v), -np.sin(v)], [np.sin(v), np.cos(v)]], int)
        waypoint = R.dot(waypoint)


print("Part 2: ", currentPos, sum(abs(currentPos)))
