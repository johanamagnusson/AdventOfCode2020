
import math

with open("data", "r") as fh:
    lines = fh.read().splitlines()

depart = int(lines[0])
busIds = [int(i) for i in lines[1].split(",") if i != "x"]
als = []
offset = 0
for bus in lines[1].split(","):
    if bus != "x":
        als.append(int(bus) - offset)
    offset += 1
als[0] = 0

toWait = depart
for bus in busIds:
    d = bus - (depart % bus)
    if d < toWait:
        toWait = d
        ID = bus

print("Part 1: ", ID, toWait, ID * toWait)



# Solve by using chinese reminder theorem (brilliant.org)

def mult_inverse(a, n):
    t = 0
    r = n
    newt = 1
    newr = a
    while newr != 0:
        q = r // newr
        (t, newt) = (newt, t - q * newt)
        (r, newr) = (newr, r - q * newr)
    if r > 1:
        return False
    if t < 0:
        t += n
    return t

def chinese_reminder(als, ns):
    N = math.prod(ns)
    s = 0
    for i in range(len(als)):
        y = N // ns[i]
        z = mult_inverse(y, ns[i])
        s += (als[i] * y * z)
    return s % N

print("Part 2: ", chinese_reminder(als, busIds))
