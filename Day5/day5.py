data = [line.strip().split() for line in open('day5.txt').readlines()]

direction = [[line[0].split(','),line[2].split(',')] for line in data ]
direction = [ [[int(x1),int(y1)],[int(x2),int(y2)]] for [[x1,y1],[x2,y2]] in direction]

def dimension(direction):
    m = 0
    for [[x1,y1],[x2,y2]] in direction:
        m = max(x1, x2, y1, y2, m)
    return(m)

def diagram(direction):
    m = dimension(direction)
    return([[0 for i in range(m+1)] for j in range(m+1)])

def part1(direction):
    d = diagram(direction)
    for [[x1,y1],[x2,y2]] in direction:
        x1, x2 = min(x1,x2), max(x1,x2)
        y1,y2 = min(y1,y2), max(y1,y2)
        if x1 == x2: #same column.
            for l in range(y1,y2+1):
                d[l][x1] += 1 
        if y1 == y2: #same line
            for c in range(x1,x2+1):
                d[y1][c] += 1
    #Count the number of dangerous places.
    c = 0
    for line in d:
        for column in line:
            if column > 1:
                c+=1
    print("Part 1: ", c)
    return()

part1(direction)

def part2(direction):
    d = diagram(direction)
    for [[x1,y1],[x2,y2]] in direction:
        if x1 == x2: #same column.
            for l in range(min(y1,y2), max(y1,y2)+1):
                d[l][x1] += 1 
        if y1 == y2: #same line
            for c in range(min(x1,x2), max(x1,x2)+1):
                d[y1][c] += 1
        elif abs((x2-x1)/(y2-y1)) == 1: #diagonal
            if x1 < x2:
                if y1 < y2:
                    for i in range(x2+1-x1):
                        d[y1+i][x1+i] += 1
                else:
                    for i in range(x2+1-x1):
                        d[y1-i][x1+i] += 1
            else:
                if y1 < y2:
                    for i in range(x1+1-x2):
                        d[y1+i][x1-i] += 1
                else:
                    for i in range(x1+1-x2):
                        d[y1-i][x1-i] += 1
    #Count the number of dangerous places.
    c = 0
    for line in d:
        for column in line:
            if column > 1:
                c+=1
    print("Part 2: ", c)
    return()

part2(direction)