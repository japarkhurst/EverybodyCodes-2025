input = '''.#.##.
##..#.
..##.#
.#.##.
.###..
###.##'''

grid = {}
rows = input.split('\n')
rowCount = len(rows)
colCount = len(rows[0])
for y,row in enumerate(rows):
    for x,char in enumerate(row):
        grid[(x,y)] = 1 if char == '#' else 0

def getNeighbors(b):
    x,y = b
    neighbors = [(x+1,y+1),(x-1,y-1),(x-1,y+1),(x+1,y-1)]
    return [(x,y) for (x,y) in neighbors if 0 <= x <= colCount-1 and 0 <= y <= rowCount-1]

totalActivated = 0
for i in range(10):
    newGrid = {}
    for g,active in grid.items():
        neighbors = getNeighbors(g)
        activeNeighborCount = len([g for g in neighbors if grid[g]])
        if (active and activeNeighborCount%2 != 0) or (not active and activeNeighborCount%2 == 0):
            newGrid[g] = 1
        else:
            newGrid[g] = 0
    grid = newGrid
    activatedCount = len([g for g in grid if grid[g]])
    print(activatedCount)
    totalActivated += activatedCount
    if i%100 == 0:
        print(i)
print(totalActivated)

'''
If a tile is active, 
it will remain active in the next round if the number of active diagonal neighbours is odd. 
Otherwise, it becomes inactive.

If a tile is inactive, it will become active in the next round if the number of active diagonal neighbours is even. 
Otherwise, it remains inactive.
'''

    
input = '''#......#
..#..#..
.##..##.
...##...
...##...
.##..##.
..#..#..
#......#'''

target = ''.join(input.split('\n'))
print(target)
targetGrid = {}
rows = input.split('\n')
rowCount = len(rows)
colCount = len(rows[0])
for y,row in enumerate(rows):
    for x,char in enumerate(row):
        targetGrid[(x,y)] = 1 if char == '#' else 0
print(f'{rowCount=},{colCount=}')

grid = {}
for y in range(34):
    for x in range(34):
        grid[(x,y)] = 0
rowCount = 34
colCount = 34
def printGrid(grid,rowCount=34,colCount=34):
    #print(grid)
    for y in range(rowCount):
        row = [grid[(x,y)] for x in range(colCount)]
        print(''.join(['#' if x else '.' for x in row]))
        
def getNeighbors(b):
    x,y = b
    neighbors = [(x+1,y+1),(x-1,y-1),(x-1,y+1),(x+1,y-1)]
    return [(x,y) for (x,y) in neighbors if 0 <= x <= colCount-1 and 0 <= y <= rowCount-1]

totalActivated = 0
for i in range(1,15000):
    newGrid = {}
    for g,active in grid.items():
        neighbors = getNeighbors(g)
        activeNeighborCount = len([g for g in neighbors if grid[g]])
        if (active and activeNeighborCount%2 != 0) or (not active and activeNeighborCount%2 == 0):
            newGrid[g] = 1
        else:
            newGrid[g] = 0
    grid = newGrid
    activatedCount = len([g for g in grid if grid[g]])
    #print(activatedCount)
    #totalActivated += activatedCount
    #printGrid(grid)
    subgrid = ''.join(('#' if char else '.' for (x,y),char in grid.items() if 13 <= x <= 20 and 13 <= y <= 20))
    
    if i in (125,1017) or subgrid == target:
        print(f'{i}: {activatedCount}')
        print(subgrid)
        #print(activatedCount)
        totalActivated += activatedCount
        #printGrid(subgrid,rowCount=8,colCount=8)
        #printGrid(grid)
        
print(totalActivated)
