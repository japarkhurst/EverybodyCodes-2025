input = '''7,7,2
12,0,4
15,5,3
24,1,6
28,5,5
40,8,2'''

from math import inf
from dataclasses import dataclass
import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    def empty(self): # determine if heap is empty
        return not self.elements
    def put(self, item, priority): # add to heap, sorted by priority
        heapq.heappush(self.elements, (priority, item))
    def get(self): # return from front of heap
        return heapq.heappop(self.elements)[1]
    def __str__(self):
        return f'{self.elements}'
    def __len__(self):
        return len(self.elements)
        
windowDict = {}
width = 0
maxHeight = 0
for row in input.split('\n'):
    col,start,height = [int(x) for x in row.split(',')]
    window = []
    for i in range(start,start+height):
        if (col+i)%2 != 0:
            continue
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

def getNeighbors(b):
    x,y = b
    return [(x+1,y+1),(x+1,y-1)]

start = (0,0)
targets = windowDict[width]
#print(sorted(walls))
#start,end,nodes = getNodes(walls)
#print(f'{start=},{end=},{nodes=}')
import heapq
distances = {n:float('inf') for n in grid}
distances[start]=0
pq = [(0,start)]
pq = PriorityQueue()
pq.put(start,0)
while pq:
    c_dist,c_node = heapq.heappop(pq)
    if c_node in targets:
        print(distances[c_node])
        break
    #if c_dist > distances[c_node]:
        #continue
    #print(f'{c_node}:{c_dist}')
    for n in getNeighbors(c_node):
        #dist = c_dist + 1
        c_n_dist = distances.get(n)
        #print(f'\t{n}: {dist},{c_n_dist}')
        if not c_n_dist:
            continue
        nx,ny = n
        cx,cy = c_node
        if ny > cy:
            dist = c_dist + 1
        else:
            dist = c_dist
        if dist < c_n_dist:
            distances[n] = dist
            #print(f'\t\tUpdating from {c_n_dist} to {dist}')
            #heapq.heappush(pq,(dist,n))
            pq.put(n,dist)
#print(len(nodes))
#print(distances[end])
