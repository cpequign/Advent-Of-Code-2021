data = open('day4.txt').readlines()

numbers = [i for i in data[0].strip().split(',')]
boards = [[i.split() for i in data[6*i+2:6*i+7]] for i in range(len(data)//6)]
marked = [ [[0 for i in range(5)] for i in range(5)] for board in boards]

def bingo():
    for mark in range(len(marked)):
        #Check if a row is marked.
        for line in range(5):
            if marked[mark][line] == [1,1,1,1,1]:
                return(True,mark)
        #Check if a column is marked
        for column in range(5):
            if (marked[mark][0][column]==1) and (marked[mark][1][column]==1) and (marked[mark][2][column]==1) and (marked[mark][3][column]==1) and (marked[mark][4][column]==1):
                return(True,mark)
    return(False,0)

def draw(n): #Modifies marked directly
    for board in range(len(boards)):
        for i in range(5):
            for j in range(5):
                if n == boards[board][i][j]:
                    marked[board][i][j] = 1
    return()

def sum_unmarked(mark):
    c=0
    for line in range(5):
        for column in range(5):
            if marked[mark][line][column] == 0:
                c += int(boards[mark][line][column])
    return(c)

def part1():
    for n in numbers:
        draw(n)
        test, mark = bingo()
        if test:
            s = sum_unmarked(mark)
            print("Part 1:", s*int(n))
            return()
    print("j'ai loupé un truc")
    return()

#part1()

winners = [0] * len(marked)

def bingo2(mark):
    for line in range(5):
        if marked[mark][line] == [1,1,1,1,1]:
            winners[mark] = 1
            return(True,mark)
    #Check if a column is marked
    for column in range(5):
        if (marked[mark][0][column]==1) and (marked[mark][1][column]==1) and (marked[mark][2][column]==1) and (marked[mark][3][column]==1) and (marked[mark][4][column]==1):
            winners[mark] = 1
            return(True,mark)    
    return(False,mark)

def part2():
    n_winners = 0
    for n in numbers:
        draw(n)
        for board in range(len(winners)):
            if winners[board] == 0:
                test, mark = bingo2(board)
                if test:
                    n_winners +=1
                    if n_winners == len(marked):
                        print('Part 2:', sum_unmarked(mark)*int(n))
                        return()
    return()

part2()