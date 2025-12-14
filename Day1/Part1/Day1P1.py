startingPt,key_to_door = 50,0
with open("input.txt","r") as f:
    for line in f:
        line = line.strip()
        direction = line[0]
        mvmt = int(line[1:])
        multiplier = 1 if direction == "R" else -1
        startingPt += (mvmt * multiplier)
        startingPt %= 100
        if startingPt == 0:
            key_to_door+=1
