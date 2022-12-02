file = open("./1/input.txt", "r")
lines = file.readlines()

# keeps track of the max calories an elf can have
elfMaxCalories = [0,0,0]

globalCounter = 0
elfTotalCalories = {}

for line in lines:
    # parse out return
    parsedLine = line.replace("\n", "")
    # check if the line is empty

    if parsedLine == "":
        currentCalories = elfTotalCalories[globalCounter]
        if currentCalories > elfMaxCalories[0]:
            elfMaxCalories[2] = elfMaxCalories[1]
            elfMaxCalories[1] = elfMaxCalories[0]
            elfMaxCalories[0] = currentCalories
        elif currentCalories > elfMaxCalories[1]:
            elfMaxCalories[2] = elfMaxCalories[1]
            elfMaxCalories[1] = currentCalories
        elif currentCalories > elfMaxCalories[2]:
            elfMaxCalories[2] = currentCalories
        globalCounter += 1
    else:
        if(globalCounter not in elfTotalCalories):
            elfTotalCalories[globalCounter] = int(parsedLine)
        else:
            elfTotalCalories[globalCounter] += int(parsedLine)

print(sum(elfMaxCalories))