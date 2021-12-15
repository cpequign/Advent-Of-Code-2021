def read_data2():
    d={}
    dist={}
    for i,l in enumerate(open('day15.txt')):
        for j,e in enumerate(l.strip()):
            e=int(e)
            d[i,j]=e
    d=create_map(d)
    s=sum([d[i] for i in d])
    for i,j in d:
        dist[i,j]=s
    return(d,dist)

def create_map(d):
    a=int(len(d)**0.5)
    for i in range(a):
        for j in range(a):
            for k in range(5):
                for l in range(5):
                    newi,newj=i+a*k,j+a*l
                    d[newi,newj]=d[i,j]+k+l
                    if d[newi,newj]>9:
                        d[newi,newj]-=9
    return(d)

def create_table(d):
    a=int(len(d)**0.5)
    t=[[0 for _ in range(a)] for _ in range(a)]
    for i,j in d:
        t[i][j]=d[i,j]
    return(t)

def partX(p2=False):
    if p2:
        d,_ = read_data2()
        d = create_table(d)
    else:
        d = [[int(i) for i in l.strip()] for l in open('day15.txt')]
    to_do_list = [(0,0)]
    s=sum([sum([d[i][j] for j in range(len(d[0]))]) for i in range(len(d))])
    dist = [[s for __ in range(len(d[0]))] for _ in range(len(d))]
    dist[0][0]=0
    while to_do_list:
        i,j=to_do_list.pop(0)
        if i<len(d)-1: #Move South
            if dist[i][j]+d[i+1][j]<dist[i+1][j]:
                dist[i+1][j]=dist[i][j]+d[i+1][j]
                to_do_list.append((i+1,j))
        if j<len(d[0])-1: #Move East
            if dist[i][j]+d[i][j+1]<dist[i][j+1]:
                dist[i][j+1]=dist[i][j]+d[i][j+1]
                to_do_list.append((i,j+1))
        if i>0: #Move North
            if dist[i][j]+d[i-1][j]<dist[i-1][j]:
                dist[i-1][j]=dist[i][j]+d[i-1][j]
                to_do_list.append((i-1,j))
        if j>0: #Move West
            if dist[i][j]+d[i][j-1]<dist[i][j-1]:
                dist[i][j-1]=dist[i][j]+d[i][j-1]
                to_do_list.append((i,j-1))
    a=2 if p2 else 1
    print(f"Part {a}:",dist[-1][-1])
    return()
import time
s=time.time()
partX()
print(time.time()-s,'seconds')
s=time.time()
partX(True)
print(time.time()-s,'seconds')