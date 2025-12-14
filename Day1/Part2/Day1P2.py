startingPt, key_to_door = 50,0
with open("input.txt","r") as f:
    for i in f:
        line = i.strip()
        direction = line[0]
        mvmt = int(line[1:])
        multiplier = 1 if direction == "R" else -1
        target = startingPt + (mvmt * multiplier)
        crossings = abs(target // 100 - startingPt // 100)
        key_to_door += crossings
        startingPt = target

print(key_to_door)
print(startingPt)