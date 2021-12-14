from collections import defaultdict
def default():
    return([])
def read_data():
    d = open('day12.txt').readlines()
    n = defaultdict(default)
    for e in d:
        l=e.strip().split('-')
        if l[0]=='start':
            n['start'].append(l[1])
        else:
            n[l[0]].append(l[1])
            n[l[1]].append(l[0])
    n[0] = 0
    return(n)

         
def path(cave,p,n):
    for e in n[cave]:
        if e=='end':
            n[0] += 1
            print(n[0])
        else:
            if e!='start':
                if e.islower():
                    if p.count(e)<1:
                        path(e,p+[e],n)
                else:
                    path(e,p+[e],n)
    return()

n = read_data()
path('start',['start'],read_data())

def path2(cave,p,m,low):
    for e in n[cave]:
        if e=='end':
            n[0]+=1
            print(n[0])
        else:
            if e!='start':
                if e.islower():
                    if p.count(e)<1:
                        path2(e,p+[e],m,low)
                    elif p.count(e)<2 and low==0:
                        path2(e,p+[e],m,1)
                else:
                    path2(e,p+[e],m,low)
    return()

m = read_data()
path2('start',['start'],m,0)