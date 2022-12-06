file = open("./6/input.txt", "r")
lines = file.readlines()
counter = 14

buffer = lines[0].strip()

window = list(buffer[:14])

while counter < len(buffer):
    del window[0]
    window.append(buffer[counter])
    if len(set(window)) == 14:
        break

    counter += 1

print(counter+1)
