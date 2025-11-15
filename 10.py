input = '''...SSS.......
.S......S.SS.
..S....S...S.
..........SS.
..SSSS...S...
.....SS..S..S
SS....D.S....
S.S..S..S....
....S.......S
.SSS..SS.....
.........S...
.......S....S
SS.....S..S..'''

input = '''..SSS##.....
.S#.##..S#SS.
..S.##.S#..S.
.#..#S##..SS.
..SSSS.#.S.#.
.##..SS.#S.#S
SS##.#D.S.#..
S.S..S..S###.
.##.S#.#....S
.SSS.#SS..##.
..#.##...S##.
.#...#.S#...S
SS...#.S.#S..'''

rows = input.split('\n')
row_count = len(rows)
col_count = len(rows[0])
                
sheep = set()
dragons = set()
hideouts = set()
cDict = {}
for y,row in enumerate(rows):
    for x,char in enumerate(row):
        cDict[(x,y)] = char
        if char == 'S':
            sheep.add((x,y))
        elif char == '#':
            hideouts.add((x,y))
        elif char == 'D':
            dragons.add((x,y))

def getMoves(xy):
    x,y = xy
    newMoves = set()
    newMoves.add((x+2,y+1))
    newMoves.add((x+1,y+2))
    newMoves.add((x-1,y+2))
    newMoves.add((x-2,y+1))
    newMoves.add((x-2,y-1))
    newMoves.add((x-1,y-2))
    newMoves.add((x+1,y-2))
    newMoves.add((x+2,y-1))
    
    return {(x,y) for x,y in newMoves if 0 <= x < col_count and 0 <= y < row_count}

def getMovedSheep(sheep):
    return {(x,y+1) for x,y in sheep if 0 <= x < col_count and 0 <= y+1 < row_count}

input = '''...SSS.......
.S......S.SS.
..S....S...S.
..........SS.
..SSSS...S...
.....SS..S..S
SS....D.S....
S.S..S..S....
....S.......S
.SSS..SS.....
.........S...
.......S....S
SS.....S..S..'''

input = '''..SSS##.....
.S#.##..S#SS.
..S.##.S#..S.
.#..#S##..SS.
..SSSS.#.S.#.
.##..SS.#S.#S
SS##.#D.S.#..
S.S..S..S###.
.##.S#.#....S
.SSS.#SS..##.
..#.##...S##.
.#...#.S#...S
SS...#.S.#S..'''

rows = input.split('\n')
row_count = len(rows)
col_count = len(rows[0])
                
sheep = set()
dragons = set()
hideouts = set()
cDict = {}
for y,row in enumerate(rows):
    for x,char in enumerate(row):
        cDict[(x,y)] = char
        if char == 'S':
            sheep.add((x,y))
        elif char == '#':
            hideouts.add((x,y))
        elif char == 'D':
            dragons.add((x,y))

def getMoves(xy):
    x,y = xy
    newMoves = set()
    newMoves.add((x+2,y+1))
    newMoves.add((x+1,y+2))
    newMoves.add((x-1,y+2))
    newMoves.add((x-2,y+1))
    newMoves.add((x-2,y-1))
    newMoves.add((x-1,y-2))
    newMoves.add((x+1,y-2))
    newMoves.add((x+2,y-1))
    
    return {(x,y) for x,y in newMoves if 0 <= x < col_count and 0 <= y < row_count}

def getMovedSheep(sheep):
    return {(x,y+1) for x,y in sheep if 0 <= x < col_count and 0 <= y+1 < row_count}

from copy import deepcopy
initialSheep = deepcopy(sheep)
initialSheepCount = len(initialSheep)
print(initialSheepCount)
round_count = 3
reachable = dragons
for i in range(round_count):
    for c in deepcopy(reachable):
        reachable.update(getMoves(c))
sheep_in_range = {x for x in reachable if x in sheep}
print(len(sheep_in_range))


    
from copy import deepcopy
initialSheep = deepcopy(sheep)
initialSheepCount = len(initialSheep)
print(initialSheepCount)
round_count = 3
reachable = dragons
for i in range(round_count):
    new = set()
    #for c in deepcopy(reachable):
        #reachable.update(getMoves(c))
    for c in reachable:
        new.update(getMoves(c))
    reachable = deepcopy(new)
    print(len(reachable))
    sheep = {s for s in sheep if s not in reachable or s in hideouts}
    sheep = getMovedSheep(sheep)
    sheep = {s for s in sheep if s not in reachable or s in hideouts}
    print(len(sheep))
sheepEaten = {s for s in initialSheep if s not in sheep}
print(len(sheepEaten))
#print(len(reachable))
sheep_in_range = {x for x in reachable if x in sheep}
print(len(sheep_in_range))


    
