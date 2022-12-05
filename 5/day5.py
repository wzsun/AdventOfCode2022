file = open("./5/input.txt", "r")
lines = file.readlines()
total = ""
lineWhereStackImageEnds = 0
stacks = {}
counter = 1

# split the parsed file into the image and the operations
for line in lines:
    parsedLine = line.replace("\n", "")

    if len(parsedLine.split("1")) > 1:
        break

    # fill stacks
    while len(parsedLine) > 0:
        container = parsedLine[:4].strip()
        if(len(container) > 0):
            containerValue = container[1:len(container)-1]
            if counter in stacks:
                stacks[counter].insert(0,containerValue)
            else:
                stacks[counter] = [containerValue]
        parsedLine = parsedLine[4:]
        counter += 1

    # reset charCounter
    counter = 1
    lineWhereStackImageEnds += 1


def getSteps(items):
    return [items[1],items[3],items[5]]

for line in lines[lineWhereStackImageEnds+2:]:
    moveAmount,fromDestination,toDestination = map(int,getSteps(line.strip().split(" ")))

    # part 1
    # for i in range(0,moveAmount):
    #     stacks[toDestination].append(stacks[fromDestination].pop())

    # part 2
    stacks[toDestination] = stacks[toDestination] + stacks[fromDestination][-moveAmount:]
    stacks[fromDestination] = stacks[fromDestination][:-moveAmount]
    print(stacks[fromDestination])

for stackLine in range(1,len(stacks)+1):
    total += stacks[stackLine][-1]

print(total)