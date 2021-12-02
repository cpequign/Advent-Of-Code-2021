values = open("day1.txt","r").readlines()

c = 0
for i in range(1,len(values)):
    if int(values[i-1])<int(values[i]):
        c+=1

print("Part 1 : ", c)

c = 0
for i in range(3,len(values)):
    if int(values[i-3])<int(values[i]):
        c+=1
    
print("Part 2 : ", c)
