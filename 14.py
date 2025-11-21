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


input = '''########
##.##.##
#......#
##.##.##
##.##.##
#......#
##.##.##
########'''

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

results = {}
repeatFound = False
totalActivated = 0
for i in range(1,6000):
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
    subgrid = ''.join(('#' if char else '.' for (x,y),char in grid.items() if 13 <= x <= 20 and 13 <= y <= 20))
    
    if subgrid == target:
        print(f'{i}: {activatedCount}')
        if activatedCount in results.values():
            repeatFound=True
            repeatIndex = i
            repeatValue = activatedCount
            break
        results[i] = activatedCount
        totalActivated += activatedCount
    if repeatFound:
        break
        #print(subgrid)
print(results)       
print(f'{repeatIndex}:{repeatValue}')

sum(results.values())
fullRepeatActivated = sum(results.values())
firstIndex = [k for k,v in results.items() if v == repeatValue][0]
fullRepeatLength = repeatIndex-firstIndex
print(fullRepeatLength)

fullRepeatCount = (rounds - firstIndex)//fullRepeatLength
print(fullRepeatCount)

rounds = 1000000000
fullRepeatCount,remainder = divmod((rounds - firstIndex),fullRepeatLength)
print(fullRepeatCount)
print(remainder)

additions = 0
for i in range(1,remainder+1):
    if i in results:
        additions+=results[i]
        print(results[i])
print(additions)

total = fullRepeatCount*fullRepeatActivated + additions
print('---')
print(total)
