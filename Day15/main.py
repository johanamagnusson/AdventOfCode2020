

testdata = [
        [0,3,6],
        [1,3,2],
        [2,1,3],
        [1,2,3],
        [2,3,1],
        [3,2,1],
        [3,1,2]]

#data = testdata[0]
data = [5,2,8,16,18,0,1]


# spoken[spokennumber] = [lastTurnSpoken, 2ndLastTurnSpoken]
spoken = {}

i = 1
for num in data[:-1]:
    spoken[num] = [i, 0]
    i += 1

# Starting numbers are uniue
prev = data[-1]
curr = 0
for turn in range(len(data)+1, 30000001):
    if prev in spoken.keys():
        spoken[prev][1] = spoken[prev][0]
        spoken[prev][0] = turn - 1
        curr = spoken[prev][0] - spoken[prev][1]
        prev = curr
    else:
        spoken[prev] = [turn - 1, 0]
        curr = 0
        prev = curr


