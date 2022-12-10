file = open("./10/input.txt", "r")
lines = file.readlines()

x = 1
cycle = 0
waitingToAdd = []
t = []

while cycle < 240:

    if cycle < len(lines):
        line = lines[cycle].split()
        if line[0] == "noop":
            waitingToAdd.insert(0,{"instruction": "noop", "wait": 1})
        elif line[0] == "addx":
            waitingToAdd.insert(0,{"instruction": "addx", "wait": 2, "value": int(line[1])})

    cycle += 1
    
    # calculate signal strength
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
        # print(cycle, x)
        t.append(cycle * x)

    # print crt
    if cycle%40 >= x and cycle%40 <= x+2:
        print("#", end="")
    else:
        print(".",end="")
    if cycle % 40 == 0:
        print()

    # run operation
    val = waitingToAdd.pop()
    if val["wait"] -1 == 0:
        # print(val)
        if val["instruction"] == "addx":
            x += val["value"]
    else:
        val["wait"] -= 1
        waitingToAdd.append(val)

total = t[0]
for x in range(1,len(t)):
    total += t[x]

# print(total)