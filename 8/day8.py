from operator import mul
from functools import reduce
file = open("./8/input.txt", "r")
lines = file.readlines()

trees = []
seenTrees = []
scenicScoreTrees = []

for x in range(0, len(lines)):
    line = lines[x].strip()
    trees.append(list(map(int, list(line))))

    if x == 0 or x == len(line)-1:
        vis = [1] * len(line)
    else:
        vis = [1] + ([0] * (len(line)-2)) + [1]
    seenTrees.append(vis)
    tempList = []
    for i in range(0,len(line)):
        tempList.append([])
    scenicScoreTrees.append(tempList)

# look left and right
for y in range(0, len(trees)):
    max = 0
    for x in range(0, len(trees[y])):
        # print(trees[y][x], end="")
        if x == 0:
            max = trees[y][x]
        else:
            if trees[y][x] > max:
                max = trees[y][x]
                seenTrees[y][x] = 1

        counter = 0
        for x2 in range(x+1, len(trees[y])):
            if trees[y][x] > trees[y][x2]:
                counter+=1
            else:
                counter+=1
                break
        scenicScoreTrees[y][x].append(counter)
    max = 0
    for x in reversed(range(0, len(trees[y]))):
        if x == 0:
            max = trees[y][x]
        else:
            if trees[y][x] > max:
                max = trees[y][x]
                seenTrees[y][x] = 1
        counter = 0
        for x2 in reversed(range(0, x)):
            if trees[y][x] > trees[y][x2]:
                counter+=1
            else:
                counter+=1
                break
        scenicScoreTrees[y][x].append(counter)

# look up and down
for y in range(0, len(trees)):
    max = 0
    for x in range(0, len(trees[y])):
        # print(trees[x][y], end="")
        if x == 0:
            max = trees[x][y]
        else:
            if trees[x][y] > max:
                max = trees[x][y]
                seenTrees[x][y] = 1
        
        counter = 0
        for x2 in range(x+1, len(trees[y])):
            if trees[x][y] > trees[x2][y]:
                counter+=1
            else:
                counter+=1
                break
        scenicScoreTrees[x][y].append(counter)
    max = 0
    for x in reversed(range(0, len(trees[y]))):
        if x == 0:
            max = trees[x][y]
        else:
            if trees[x][y] > max:
                max = trees[x][y]
                seenTrees[x][y] = 1

        counter = 0
        for x2 in reversed(range(0, x)):
            if trees[x][y] > trees[x2][y]:
                counter+=1
            else:
                counter+=1
                break
        scenicScoreTrees[x][y].append(counter)

t = 0
for x in range(0,len(seenTrees)):
    # print(scenicScoreTrees[x], trees[x])
    for y in range(0, len(seenTrees[x])):
        if seenTrees[x][y] == 1:
            t += 1

maxScenic = 0
for x in range(0, len(scenicScoreTrees)):
    for y in range(0, len(scenicScoreTrees[x])):
        score = reduce(mul, scenicScoreTrees[x][y], 1)
        if score > maxScenic:
            maxScenic = score

print(maxScenic)