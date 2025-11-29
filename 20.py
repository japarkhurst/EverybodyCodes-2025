input = '''T#TTT###T##
.##TT#TT##.
..T###T#T..
...##TT#...
....T##....
.....#.....'''

from math import inf
from collections import defaultdict
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

@dataclass
class Node:
    xy: tuple
    dist: int = inf
    def __lt__(self,item):
        return self.dist < item.dist

def isEven(num):
    if num % 2 == 0:
        return True

tList = set()
rows = input.split('\n')
for y,row in enumerate(rows):
    for x,char in enumerate(row):
        if char in ('T','S','E'):
            tList.add((x,y))
        if char == 'S':
            startXY = (x,y)
        if char == 'E':
            endXY = (x,y)
print(tList)

cnt = 0
neighbors = defaultdict(set)
for (tx,ty) in tList:
    if (tx+1,ty) in tList:
        cnt += 1
        neighbors[(tx,ty)].add((tx+1,ty))
        neighbors[(tx+1,ty)].add((tx,ty))
    if isEven(ty) and not isEven(tx) and (tx,ty+1) in tList:
        cnt += 1
        neighbors[(tx,ty)].add((tx,ty+1))
        neighbors[(tx,ty+1)].add((tx,ty))
    if not isEven(ty) and isEven(tx) and (tx,ty+1) in tList:
        cnt += 1
        neighbors[(tx,ty)].add((tx,ty+1))
        neighbors[(tx,ty+1)].add((tx,ty))
print(cnt)

grid = {(x,y):Node(xy=(x,y)) for (x,y) in tList}
start = grid[startXY]
distances = {n:float('inf') for n in grid}
distances[start.xy]=0
pq = PriorityQueue()
start.dist = 0
pq.put(start,0)
while pq:
    c = pq.get()
    if c.xy == targetXY:
        print(distances[c])
        break
    for n in getNeighbors(c):
        #dist = c_dist + 1
        c_n_dist = distances.get(n)
        #print(f'\t{n}: {dist},{c_n_dist}')
        if not c_n_dist:
            continue
        dist = c.dist + 1
        if dist < c_n_dist:
            distances[n] = dist
            grid[n].dist = dist
            pq.put(grid[n],dist)
#print(len(nodes))
#print(distances[end])
#result = min(dist for c,dist in distances.items() if c[0] == width)+1
#print(result)
