file = open("./3/input.txt", "r")
lines = file.readlines()
total = 0
cachedLines = []
numberOfBadges = 3
sackItemMap = {}

def getValueOfLetter(letter):
    if ord(letter) > ord("Z"):
        return ord(letter)-ord("a")+1
    else:
        return ord(letter)-ord("A")+27

for line in lines:
    parsedLine = line.replace("\n","")
    cachedLines.append(parsedLine)
    for item in parsedLine:
        if len(cachedLines) == 1:
            sackItemMap[item] = len(cachedLines)
        elif item in sackItemMap and sackItemMap[item] == (len(cachedLines) - 1):
            sackItemMap[item] = len(cachedLines)

    if len(cachedLines) == numberOfBadges:
        for item in sackItemMap:
            if sackItemMap[item] == numberOfBadges:
                total += getValueOfLetter(item)
        cachedLines = []
        sackItemMap = {}

print(total)