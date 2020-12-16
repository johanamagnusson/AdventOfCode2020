
with open("data", "r") as fh:
    lines = fh.read().splitlines()

fields = {} # (a,b,c,d) a - b or c - d
yourTicket = []
nearbyTickets = []


state = 0
for line in lines:
    if line == "":
        continue
    elif "your" in line:
        state = 1
        continue
    elif "nearby" in line:
        state = 2
        continue
    if state == 0:
        fields[line.split(": ")[0]] = []
        s = line.split(": ")[1].split(" or ")
        fields[line.split(": ")[0]] = [int(s[0].split("-")[0]), int(s[0].split("-")[1]),
            int(s[1].split("-")[0]), int(s[1].split("-")[1])]
    elif state == 1:
        yourTicket = [int(x) for x in line.split(",")]
    elif state == 2:
        nearbyTickets.append([int(x) for x in line.split(",")])


validValues = []
invalidValues = []
invalidTickets = []
for ticket in nearbyTickets:
    validValues.append([])
    for value in ticket:
        for rule in fields.values():
            if (rule[0] <= value <= rule[1]) or (rule[2] <= value <= rule[3]):
                if value not in validValues[-1]:
                    validValues[-1].append(value)
        if value not in validValues[-1]:
            invalidValues.append(value)
            if ticket not in invalidTickets:
                invalidTickets.append(ticket)


print("Part 1: ", sum(invalidValues))

#print(fields)
#print(invalidTickets)
#print(nearbyTickets)
print(len(yourTicket), len(fields))

for ticket in invalidTickets:
    nearbyTickets.remove(ticket)

candidates = []
for i in range(len(yourTicket)):
    candidates.append(list(fields.keys()))

unassignedFields = list(fields.keys())

while unassignedFields:
    for i in range(len(yourTicket)):
        if len(candidates[i]) == 1:
            for k in range(len(candidates)):
                if k != i and  candidates[i][0] in candidates[k]:
                    candidates[k].remove(candidates[i][0])
            if candidates[i][0] in unassignedFields:
                unassignedFields.remove(candidates[i][0])
            continue
        for ticket in nearbyTickets:
            for j in range(len(nearbyTickets)):
                value = nearbyTickets[j][i]
                for field in unassignedFields:
                    rule = fields[field]
                    if not ((rule[0] <= value <= rule[1]) or (rule[2] <= value <= rule[3])):
                        if field in candidates[i]:
                            candidates[i].remove(field)

print(candidates)
prod = 1
for field, value in zip(candidates, yourTicket):
    if "departure" in field[0]:
        print(field[0], value)
        prod *= value

print("Part 2: ", prod)
