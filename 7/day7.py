file = open("./7/input.txt", "r")
lines = file.readlines()
fileSystem = {"/": {"size": 0}}
location = ["/"]
counter = 0
total = {"size": 0}
totalDiskSpace = 70000000
updateSize = 30000000
part2Total = {"size": totalDiskSpace}


def part2(fs, folderSizeLessThen, part2Total, previousItem=None):
    for item in fs:
        if item == "size" and fs[item] > folderSizeLessThen:
            # print( previousItem, item, fs[item])
            if fs[item] < part2Total["size"]:
                part2Total["size"] = fs[item]
        if type(fs[item]) is dict:
            part2(fs[item], folderSizeLessThen, part2Total, item)


def part1(fs, total):
    for item in fs:
        if item == "size" and fs[item] < 100000:
            total["size"] += fs["size"]
        if type(fs[item]) is dict:
            part1(fs[item], total)


def printFileSystem(fs, c):
    for item in fs:
        print("  " * c, item, fs[item])
        if type(fs[item]) is dict:
            printFileSystem(fs[item], c+1)


def updateFileSystem(k1, k2, updateSize=False):
    pointer = fileSystem[location[0]]
    if updateSize:
        pointer["size"] += int(k2)

    for item in location[2:]:
        pointer = pointer[item]
        if updateSize:
            pointer["size"] += int(k2)
    pointer[k1] = k2


while counter < len(lines):
    parsedLine = lines[counter][:-1]
    # print(parsedLine, fileSystem)
    if parsedLine[0] == "$":
        command = parsedLine[2:4]
        if command == "cd":
            changedLocation = parsedLine[5:]
            if changedLocation == "..":
                location.pop()
            else:
                location.append(changedLocation)
            counter += 1
        elif command == "ls":
            start = True
            # increment to next line
            counter += 1
            while start == True and counter < len(lines):
                if lines[counter][0] == "$":
                    start = False
                    break
                else:
                    file = lines[counter].strip().split(" ")
                    if file[0] == "dir":
                        updateFileSystem(file[1], {"size": 0})
                    else:
                        updateFileSystem(file[1], file[0], True)
                counter += 1

# printFileSystem(fileSystem, 0)
part2(fileSystem, updateSize - (totalDiskSpace -
      fileSystem["/"]["size"]), part2Total=part2Total)
print(part2Total)
