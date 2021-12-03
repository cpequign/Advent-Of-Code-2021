data = [line.split("\n")[0] for line in open("day3.txt").readlines()]
n = len(data[0])
l = [0 for i in range(n)]
for d in data:
    for i in range(n):
        l[i] += int(d[i])

gamma = [int(l[i]>(len(data)/2)) for i in range(n)]
epsilon = [int(l[i]<=(len(data)/2)) for i in range(n)]

def list2int(l):
    c = 0
    for e in l:
        c = 2*c + e
    return(c)

print("Part1 : ", list2int(gamma)*list2int(epsilon))

def most_common(data,pos):
    c = 0
    for d in data:
        c += int(d[pos])
    return(int(c>=len(data)/2))

def ox(data,pos):
    if len(data)==1:
        return(data[0])
    b = most_common(data,pos)
    data2 = []
    for d in data:
        if int(d[pos]) == b:
            data2.append(d)
    return(ox(data2,pos+1))

def least_common(data,pos):
    c = 0
    for d in data:
        c += int(d[pos])
    return(1-int(c>=len(data)/2))    

def co(data,pos):
    if len(data)==1:
        return(data[0])
    b = least_common(data,pos)
    data2 = []
    for d in data:
        if int(d[pos]) == b:
            data2.append(d)
    return(co(data2,pos+1))   

print("Part2 : ", int(ox(data,0),2)*int(co(data,0),2))