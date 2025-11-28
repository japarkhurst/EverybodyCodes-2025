input = '''7,7,2
12,0,4
15,5,3
24,1,6
28,5,5
40,8,2'''

windowDict = {}
width = 0
maxHeight = 0
for row in input.split('\n'):
    col,start,height = [int(x) for x in row.split(',')]
    window = []
    for i in range(start,start+height):
        window.append((col,i))
    windowDict[col] = window
    width = col
    maxHeight = max(i,maxHeight)
print(width,maxHeight)
print(windowDict)

from dataclasses import dataclass
@dataclass
class Cell():
    xy: tuple[int]
    dir: int = None
    
grid = {}
for x in range(1,width+1):
    for y in range(1,maxHeight+1):
        if (x+y)%2 != 0:
            continue
        if x in windowDict:
            window = windowDict[x]
            for w in window:
                grid[(w)] = Cell(w)
        else:
            grid[(x,y)] = Cell((x,y))
print(grid)

