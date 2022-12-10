file = open("./9/test.txt", "r")
lines = file.readlines()
out = open("./9/out.txt", "w")

# set up grid
rows, cols = (20, 20)
grid = [[0 for i in range(cols)] for j in range(rows)]

# position of rope
rope = [[rows//2, rows//2], [rows//2, rows//2],[rows//2, rows//2], [rows//2, rows//2],[rows//2, rows//2], [rows//2, rows//2],[rows//2, rows//2], [rows//2, rows//2],[rows//2, rows//2], [rows//2, rows//2],]
lastCommand = ["none", "none","none", "none","none", "none","none", "none","none", "none",]
# item[0] is useless
lastSeenHead = [[rows//2, rows//2], [rows//2, rows//2],[rows//2, rows//2], [rows//2, rows//2],[rows//2, rows//2], [rows//2, rows//2],[rows//2, rows//2], [rows//2, rows//2],[rows//2, rows//2], [rows//2, rows//2],]


def moveKnot(pos):
    global lastCommand
    global rope
    global lastSeenHead
    canSeeHead = False

    # how to pass by reference for this?
    # head = rope[pos-1]
    # tail = rope[pos]
    # lastSeenHeadLocal = lastSeenHead[pos]
    # lastCommandLocal = lastCommand[pos]

    # check if head is around tail
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
        "dtright": (-1, 1),
        "dtleft": (-1, -1),
        "dbright": (1, 1),
        "dbleft": (1, -1),
        "none": (0, 0)
    }
    for d in directions:
        if rope[pos-1][0] == directions[d][0]+rope[pos][0] and rope[pos-1][1] == directions[d][1]+rope[pos][1]:
            lastCommand[pos] = d
            lastSeenHead[pos][0] = rope[pos-1][0]
            lastSeenHead[pos][1] = rope[pos-1][1]
            canSeeHead = True
            break

    if canSeeHead == False:
        # if last known position was diagonal
        if lastCommand[pos][0] == "d":
            rope[pos][0] = lastSeenHead[pos][0]
            rope[pos][1] = lastSeenHead[pos][1]
        else:
            rope[pos][0] += directions[lastCommand[pos]][0]
            rope[pos][1] += directions[lastCommand[pos]][1]
        
        # update last seen list when a node can't be seen
        for x in range(1, len(rope)):
            lastSeenHead[x][0] = rope[x-1][0]
            lastSeenHead[x][1] = rope[x-1][1]

    print(pos, "lastseen", canSeeHead, lastSeenHead)
    print(pos, rope)

    if pos == len(rope)-1:
        grid[rope[pos][0]][rope[pos][1]] = 1


for line in lines:
    direction, amount = line.split()
    amount = int(amount)
    head = rope[0]
    if direction == "R":
        for x in range(0, amount):
            head[1] += 1
            for knot in range(1, len(rope)):
                moveKnot(knot)
    elif direction == "U":
        for x in range(0, amount):
            head[0] -= 1
            for knot in range(1, len(rope)):
                moveKnot(knot)
    elif direction == "L":
        for x in range(0, amount):
            head[1] -= 1
            for knot in range(1, len(rope)):
                moveKnot(knot)
    elif direction == "D":
        for x in range(0, amount):
            head[0] += 1
            for knot in range(1, len(rope)):
                moveKnot(knot)
    else:
        print("error")
    
    print()
    print(direction, amount, rope)
    print("last seen", lastSeenHead)
    print()

t = 0
for x in range(0, len(grid)):
    for y in range(0, len(grid[x])):
        if grid[x][y] == 1:
            t += 1

for line in grid:
    out.write("".join(map(str, line)) + "\n")

print(t)
