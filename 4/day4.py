file = open("./4/input.txt", "r")
lines = file.readlines()
total = 0

def contains(a1,a2):
    if int(a1[1]) >= int(a2[1]) and int(a1[0]) <= int(a2[0]):
        return True
    elif int(a2[1]) >= int(a1[1]) and int(a2[0]) <= int(a1[0]):
        return True

    return False

def overlaps(a1,a2):
    a1set = set(range(int(a1[0]), int(a1[1])+1))
    a2set = set(range(int(a2[0]), int(a2[1])+1))
    intersect = a1set & a2set

    if len(intersect) > 0:
        return True
    
    return False


for elfCleaningPair in lines:
    [elf1, elf2] = elfCleaningPair.strip().split(",")
    elf1Area = elf1.split("-")
    elf2Area = elf2.split("-")

    if overlaps(elf1Area, elf2Area):
        total += 1

print(total)
