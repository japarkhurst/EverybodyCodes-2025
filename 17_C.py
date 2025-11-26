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

@dataclass
class Node:
    #id: int
    xy: tuple
    cost: int
    dist: int = inf
    #parent: int = None
    def __lt__(self,item):
        return self.dist < item.dist

def getNeighbors(c,coords):
    x,y=c
    adj = [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
    return [c for c in adj if c in coords]

def calcDist(current,new):
    return current.dist + new.char

rows = input.split('\n')
rowCount = len(rows)
colCount = len(rows[0])
R = 10
charDict = {}
for y,row in enumerate(rows):
    for x,char in enumerate(row):
        if char == '@':
            V = (x,y)
        elif char == 'S':
            S = (x,y)
        else:
            charDict[(x,y)] = int(char)
Xv,Yv = V
Xs,Ys = S

R = max(rowCount,colCount)
burnDict = {}
priorBurned = 0
for i in range(1,R+1):
    burned = sum(num for (Xc,Yc),num in charDict.items() if (Xv - Xc) * (Xv - Xc) + (Yv - Yc) * (Yv - Yc) <= i * i)
    burnDict[i] = burned-priorBurned
    priorBurned=burned
print(burnDict)
maxBurnRound = max(burnDict,key=lambda x:burnDict[x])
result = maxBurnRound * burnDict[maxBurnRound]
print(result)

Nodes = [Node(xy=c,cost=cost) for c,cost in charDict.items()]
nDict = {(n.xy):n for n in Nodes}
PENDING = PriorityQueue()
source = [n for n in Nodes if n.xy == S][0]
source.dist = 0
PENDING.put(source,0)
maxi = 10000
i = 0

print(f'{source=},{targetXY=}')
# define adjacent
# same coordinate but different direction (distance is 1000)
# adjacent coordinate and same direction (distance is 1
#pDict = {(n.xy,n.dir):set() for n in Nodes}
while PENDING and i < maxi:
    i+=1
    #print(f'\n{i}\nPENDING Count: {len(PENDING)}')
    #print(f'\n\nPENDING: {PENDING}')
    current = PENDING.get()
    #print(f'{current=}')
    if current.xy == targetXY:
        print('Target Found')
        print(current)
        target = current
        break
    #currentID = current.id
    #neighbors = getNeighbors(current)
    #neighbors = neighborDict[current.id]
    neighbors = getNeighbors(current.xy,coords)
    #print(f'\nNeighbors for {current.xy}: {[n for n in neighbors]}')
    for n in neighbors:
        if not n:
            continue
        new = nDict[n]
        #print(new)
        #print(current)
        #if n.xy == current.xy:
            #distance = 1000
        ##else:
            #distance = 1
        new_dist = current.dist + 1
        #if new_dist == new.dist:
            #pDict[(n.xy,n.dir)].add((current.xy,current.dir))
        if new_dist < new.dist:
            #pDict[(n.xy,n.dir)].add((current.xy,current.dir))
            nDict[n].dist = new_dist
            #print(f'{n} added')
            PENDING.put(new,new_dist)
