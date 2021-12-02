data = [line.split() for line in open("day2.txt").readlines()]

forward = sum([int(units) for (direction,units) in data if direction == 'forward'])
down = sum([int(units) for (direction,units) in data if direction == 'down' ])
up = sum([int(units) for (direction,units) in data if direction == 'up' ])

print("Part1 : ",-forward*(up-down))

aim = 0
depth = 0
for (direction,units) in data:
    if direction == 'forward':
        depth += int(units)*aim
    elif direction == 'down':
        aim += int(units)
    else:
        aim -=int(units)
        
print("Part2 : ", depth*forward)