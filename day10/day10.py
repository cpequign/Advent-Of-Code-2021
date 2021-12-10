#This is the code I first wrote.
d = [l.strip() for l in open('day10.txt')]
s,p = 0,[3,57,1197,25137]
b=[]
close = ')]}>'
for l in d:
    t=True
    op = []
    for e in l:
        if e in '([{<':
            op.append(e)
        else:
            a=op.pop(-1)
            if a+e not in ['()','[]','{}','<>']:
                s+=p[close.index(e)]
                t=False
    if t:
        d=0 
        for e in op[::-1]:
            if e=='[':
                d=d*5+2
            elif e=='(':
                d=d*5+1
            elif e=='{':
                d=d*5+3
            else:
                d=d*5+4
        b.append(d)

b=sorted(b)       
print("Part 1:",s)
print("Part 2:",b[(len(b))//2])

#This is the shortened version
"""
d=[l.strip()for l in open('day10.txt')]
s,p,c,b=0,[3,57,1197,25137],')]}>',[]
for l in d:
    o,a=[],s
    for e in l:
        if e in'([{<':o.append(e)
        else:s+=p[c.index(e)]if o.pop(-1)+e not in['()','[]','{}','<>']else 0         
    if s==a:b.append(sum([(1+'([{<'.index(o[i]))*(5**i)for i in range(len(o))]))
print(s,sorted(b)[len(b)//2])
"""