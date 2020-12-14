import itertools as it

with open("data", "r") as fh:
    lines = fh.read().splitlines()

masks = []
values = []

for line in lines:
    if line[:2] == "ma":
        values.append([])
        b = 0
        maskOn = 0
        maskOff = 2 ** 36 - 1
        for c in reversed(line):
            if c == "1":
                maskOn += (2 ** b)
            elif c == "0":
                maskOff -= (2 ** b)
            b += 1
        masks.append((maskOn, maskOff))
    elif line[:2] == "me":
        address = int(line.split(" = ")[0][4:].replace("]", ""))
        value = int(line.split(" = ")[1])
        values[-1].append((address, value))




memory = {}
for mask, value in zip(masks, values):
    for item in value:
        val = item[1]
        val |= mask[0]
        val &= mask[1]
        memory[item[0]] = val


print("Part 1: ", sum(memory.values()))

masks = []
for line in lines:
    if line[:2] == "ma":
        b = 0
        maskOn = 0
        maskFloat = [0]
        for c in reversed(line):
            if c == "1":
                maskOn += (2 ** b)
            elif c == "X":
                for i in range(len(maskFloat)):
                    maskFloat.append(maskFloat[i] + 2 ** b)
            b += 1
        masks.append((maskOn, maskFloat))

def get_addresses(mask, address):
    addresses = []
    address |= mask[0]
    addresses.append(address)
    for mf in mask[1][1:]:
        addresses.append(address ^ mf)
    return addresses


memory = {}
for mask, value in zip(masks, values):
    for item in value:
        addresses = get_addresses(mask, item[0])
        for address in addresses:
            memory[address] = item[1]


print("Part 2: ", sum(memory.values()))
