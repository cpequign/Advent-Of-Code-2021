#I wanted to to it in one line and as few caracters as possible for part1
d=[[int(a)for a in l.strip()]for l in open('day9.txt')]
print(sum([1+d[i][j]for i in range(len(d))for j in range(len(d[0]))if d[i][j]<min([d[i+di][j+dj]for di,dj in[(-1,0),(1,0),(0,-1),(0,1)]if i+di in range(len(d)) and j+dj in range(len(d[0]))])]))

#Dynamic programming
def part2():
    m1,m2,m3 = 0,0,0
    low = [(i,j) for i in range(len(d))for j in range(len(d[0]))if d[i][j]<min([d[i+di][j+dj]for di,dj in[(-1,0),(1,0),(0,-1),(0,1)]if i+di in range(len(d)) and j+dj in range(len(d[0]))])]
    for i,j in low:
        visited, to_do_list = [], [(i,j)]
        while to_do_list:
            (i,j) = to_do_list.pop(0)
            if (i,j) not in visited:
                visited.append((i,j))
            to_do_list += [(i+di,j+dj)for di,dj in[(-1,0),(1,0),(0,-1),(0,1)]if i+di in range(len(d)) and j+dj in range(len(d[0])) and (i+di,j+dj) not in visited and d[i+di][j+dj]<9]
        m = len(visited)
        m1,m2,m3 = sorted([m,m1,m2,m3])[1:]
    print("Part 2:", m1*m2*m3)
    return()
part2()