input = '''989611
857782
746543
766789'''

grid = {}
queue = []
seen = set()
burned = set()

rows = input.split('\n')
rowCount = len(rows)
colCount = len(rows[0])
for y,row in enumerate(rows):
    for x,char in enumerate(row):
        grid[(x,y)] = int(char)

def getNeighbors(b):
    x,y = b
    neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    return [(x,y) for (x,y) in neighbors if 0 <= x <= colCount-1 and 0 <= y <= rowCount-1]

burned.add((0,0))
burned.add((colCount-1,rowCount-1))
queue = [(0,0)]
queue.append((colCount-1,rowCount-1))
i=0
while queue and i<20:
    i+=1
    b = queue.pop()
    b_num = grid[b]
    neighbors = getNeighbors(b)
    #print(neighbors)
    for n in neighbors:
        n_num = grid[n]
        #print(f'Comparing {n_num} and {b_num}')
        if b_num >= grid[n] and n not in seen:
            burned.add(n)
            queue.append(n)
    seen.add(b)
print(len(burned))

