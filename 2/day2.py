file = open("./2/input.txt", "r")
lines = file.readlines()
scores = {"A": 1, "B": 2, "C":3, "X": 1, "Y": 2, "Z":3, "lose": 0, "win": 6, "draw": 3}
part2Map = {"X": "lose", "Y": "draw", "Z": "win"}
totalScore = 0

# 0 = tie, 1 = p1, 2 = p2
def rpsWinner(p1, p2):
    if p1 == "A":
        if p2 == "X":
            return 0
        elif p2 == "Y":
            return 2
        elif p2 == "Z":
            return 1
    elif p1 == "B":
        if p2 == "X":
            return 1
        if p2 == "Y":
            return 0
        if p2 == "Z":
            return 2
    elif p1 == "C":
        if p2 == "X":
            return 2
        if p2 == "Y":
            return 1
        else:
            return 0

def findCorrectRpsAnswer(p1, situation):
    if p1 == "A":
        if situation == "win":
            return "Y"
        elif situation == "lose":
            return "Z"
        else:
            return "X"
    if p1 == "B":
        if situation == "win":
            return "Z"
        elif situation == "lose":
            return "X"
        else:
            return "Y"
    if p1 == "C":
        if situation == "win":
            return "X"
        elif situation == "lose":
            return "Y"
        else:
            return "Z"

for line in lines:
    parsedLine = line.replace("\n", "").split(" ")
    result = findCorrectRpsAnswer(parsedLine[0], part2Map[parsedLine[1]])
    
    totalScore += scores[result]
    totalScore += scores[part2Map[parsedLine[1]]]

print(totalScore)
