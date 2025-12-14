import time
start_time = time.time()

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
end_time = time.time()
print(key_to_door)
print(startingPt)
print(f"Time: {(end_time - start_time) * 1000:.2f} ms")

