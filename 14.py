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
