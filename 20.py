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
        if char == 'T':
            tList.add((x,y))
print(tList)

cnt = 0
for (tx,ty) in tList:
    if (tx+1,ty) in tList:
        cnt += 1
    if isEven(ty) and not isEven(tx) and (tx,ty+1) in tList:
        cnt += 1
    if not isEven(ty) and isEven(tx) and (tx,ty+1) in tList:
        cnt += 1
print(cnt)

 
