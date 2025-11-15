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

rows = input.split('\n')
row_count = len(rows)
col_count = len(rows[0]]
                
sheep = set()
dragons = set()
for y,row in enumerate(rows):
    for x,char in enumerate(row):
        cDict[(x,y)] = char
        if char == 'S':
            sheep.add((x,y))
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
    return newMoves

move_count = 3
reachable = dragons
for i in range(move_count):
    for c in reachable:
        reachable.update(newMoves)
print(len(reachable))
    


    
