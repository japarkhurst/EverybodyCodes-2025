input = '''T#TTT###T##
.##TT#TT##.
..T###T#T..
...##TT#...
....T##....
.....#.....'''

tList = set()
rows = input.split('\n')
for y,row in enumerate(rows):
    for x,char in enumerate(row):
        if char == 'T':
            tList.add((x,y))
print(tList)
