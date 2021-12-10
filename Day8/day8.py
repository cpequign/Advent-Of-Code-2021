data = [l.split(' | ') for l in open('day8.txt')]

def part1():
    c=0
    for a,b in data:
        for e in b.split():
            if len(e) in [2,3,4,7]:
                c+=1
    print("Part 1: ",c)
    return()

part1()

def find_top(l,r1,r7):
    for e in r7:
        if e not in r1:
            t = e
    return(t)

def find_tl_bl(l5):
    x,y,z= l5
    c=''
    for e in x:
        if e not in y+z:
            c+=e
    for e in y:
        if e not in x+z:
            c+=e
    for e in z:
        if e not in x+y:
            c+=e
    return(c)
    
def find_tr_br(l5,tl,r1):
    for letter in l5:
        if tl in letter:
            if r1[0] in letter:
                br = r1[0]
                tr = r1[1]
            else:
                br = r1[1]
                tr = r1[0]
    return(br,tr)

def part2():
    s=0
    for l,n in data:
        l = l.split()
        r1 = ''.join(sorted([i for i in l if len(i)==2][0]))
        r7 = ''.join(sorted([i for i in l if len(i)==3][0]))
        r4 = ''.join(sorted([i for i in l if len(i)==4][0]))
        r8 = ''.join(sorted([i for i in l if len(i)==7][0]))
        l5 = [i for i in l if len(i)==5]
        t = find_top(l,r1,r7) #The top
        tl_bl = find_tl_bl(l5) #Top-left - Bottom left
        mid = ''.join([e for e in r4 if e not in (r1+tl_bl)]) #mid
        tl = ''.join([e for e in r4 if e not in (r1+mid)]) #top left
        bl = ''.join([e for e in tl_bl if e !=tl]) #top bottom
        br,tr=find_tr_br(l5,tl,r1)
        b = ''.join([i for i in r8 if i not in (t+tr+tl+mid+br+bl)])
        r0 = ''.join(sorted([t,tl,tr,bl,br,b])) 
        r2 = ''.join(sorted([t,tr,mid,bl,b]))
        r3 = ''.join(sorted([t,tr,mid,br,b]))
        r5 = ''.join(sorted([t,tl,mid,br,b]))
        r6 = ''.join(sorted([t,tl,mid,bl,br,b]))
        r9 = ''.join(sorted([t,tl,tr,mid,br,b]))
        l = [r0,r1,r2,r3,r4,r5,r6,r7,r8,r9]
        n = n.split()
        c=''
        for e in n:
            e = ''.join(sorted(e))
            c+= str(l.index(e))
        s += int(c)
    print("Part 2: ",s)
    return()

part2()