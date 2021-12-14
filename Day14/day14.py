def read_data():
    d=open('day14.txt').readlines()
    l=[]
    for e in d:
        e=e.strip()
        if e:
            if '-' in e:
                l.append(e.split(' -> '))
            else:
                start=e
    return(start,l)

def naïve(start,l):
    new=''
    for i in range(len(start)-1):
        ab=start[i:i+2]
        for e in l:
            if e[0]==ab:
                new+=ab[0]+e[1]
    new+=start[-1]
    return(new)
    
def multiple_naïve(start,l):
    for _ in range(10):
        start=naïve(start,l)
    return(start)

def find_letters(l):
    letters=''
    for (a,b) in l:
        for e in a:
            if e not in letters:
                letters+=e
    return(letters)

def part1():
    start,l=read_data()
    new = multiple_naïve(start,l)
    mi,ma=len(new),0
    for e in find_letters(l):
        m=new.count(e)
        if m>ma:
            ma=m
        if mi>m:
            mi=m
    print('Part 1:',ma-mi)
    return()

part1()

from collections import defaultdict

def read_data2():
    data=open('day14.txt').readlines()
    l={}
    d={}
    for e in data:
        e=e.strip()
        if e:
            if '-' in e:
                e=e.split(' -> ')
                l[e[0]]=e[1]
            else:
                start=e
    for double in l:
        d[double]=0
    for i in range(len(start)-1):
        d[start[i:i+2]]+=1
    return(d,l)
    
def count_letters(d,letters):
    l=[0]*len(letters)
    for ind,e in enumerate(letters):
        for double in d:
            l[ind]+=double.count(e)*d[double]
    l=[(l[i]+1)//2 for i in range(len(l))]
    return(l)

def def_val():return(0)

def count_new_double(d,l):
    newd = defaultdict(def_val)
    for double in d:
        a,b,c=double[0],double[1],l[double]
        newd[a+c]+=d[double]
        newd[c+b]+=d[double]
    return(newd)

def part2():
    d,l = read_data2()
    for _ in range(40):
        d=count_new_double(d,l) 
    letters=find_letters(l)
    c=count_letters(d,letters)
    print('Part 2:',max(c)-min(c))
    return()

part2()