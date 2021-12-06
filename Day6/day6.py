data = [int(e) for e in open('day6.txt').readlines()[0].split(',')]
d = [0 for i in range(9)]

for e in data:
    d[e] += 1

def part(d,days=80):
    day = 0
    while day < days:
        d2 = [0 for i in range(9)]
        for e in range(len(d)):
            if e>0:
                d2[e-1] += d[e]
            else:
                d2[6] += d[0]
                d2[8] += d[0]
        d = [e for e in d2]
        day += 1
    if days == 80:
        print("Part 1:",sum(d))
    else:
        print("Part 2:",sum(d))
    return()

part(d)
part(d,256)               