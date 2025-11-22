input = 'R3,R4,L3,L4,R3,R6,R9'
input = 'L6,L3,L6,R3,L6,L3,L3,R6,L6,R6,L6,L6,R3,L3,L3,R3,R3,L6,L6,L3'
#input = 'L6,L3,L6,R6,L6,L3,R6,L6,L6,R6,L3,R6,L3,L6,R3,R6,L6,L3,R6,L6,L6,R3,R3,L6,L3,R6,L3,R6,L6,L6,R3,R6,L6,L6,R6,L6,R3,L3,R6,L3,L6,R3,L3,R3,L3,R6,L6,R6,L3,L3,R6,R6,L6,L3,R3,L3,R6,L3,R3,L3'

L,R = 'L','R'
N,S,E,W = 'N','S','E','W'
walls = []
cx,cy = (0,0)
walls.append((cx,cy))
face = N
L_Turn_Dict = {N:W,W:S,S:E,E:N}
R_Turn_Dict = {v:k for k,v in L_Turn_Dict.items()}
Move_Dict = {N:(0,1),W:(-1,0),S:(0,-1),E:(1,0)}
for inst in input.split(','):
    turn,cnt = inst[0],int(inst[1:])
    #print(f'Moving {cnt} to the {turn}')
    if turn == L:
        new_dir = L_Turn_Dict[face]
    else:
        new_dir = R_Turn_Dict[face]
    #print(f'Turning from {face} to {new_dir}')
    dx,dy = Move_Dict[new_dir]
    #print(f'Move x {dx}, y {dy}')
    for i in range(cnt):
        cx+=dx
        cy+=dy
        walls.append((cx,cy))
        #print(f'Adding ({cx},{cy})')
    face = new_dir
def getNodes(walls):
    xList = sorted({w[0] for w in walls})
    yList = sorted({w[1] for w in walls})
    start,end = walls[0],walls[-1]
    nodes = set()
    for y in range(max(yList),min(yList)-1,-1):
        row = ''
        for x in range(min(xList),max(xList)+1):
            if (x,y) == start:
                row+='S'
                nodes.add((x,y))
            elif (x,y) == end:
                row+='E'
                nodes.add((x,y))
            elif (x,y) in walls:
                row+='#'
            else:
                row+='.'
                nodes.add((x,y))
        print(row)
    return start,end,nodes

def getNeighbors(b):
    x,y = b
    return [(x+1,y+1),(x-1,y-1),(x-1,y+1),(x+1,y-1)]
 
#print(sorted(walls))
start,end,nodes = getNodes(walls)
#print(f'{start=},{end=},{nodes=}')
import heapq
distances = {n:float('inf') for n in nodes}
distances[start]=0
pq = [(0,start)]
while pq:
    c_dist,c_node = heapq.heappop(pq)
    #if c_dist > distances[c_node]:
        #continue

    for n in getNeighbors(c_node):
        dist = c_dist + 1
        c_n_dist = distances.get(n)
        print(f'{n}: {dist},{c_n_dist}')
        if not c_n_dist:
            continue
        if dist < c_n_dist:
            distances[n] = dist
            heapq.heappush(pq,(dist,n))
print(len(nodes))
print(distances[end])
