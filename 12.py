input = '''989611
857782
746543
766789'''

grid = {}
q = []
seen = set()

rows = input.split('\n')
for y,row in enumerate(rows):
    for x,char in enumerate(row):
        grid[(x,y)] = int(char)
        
