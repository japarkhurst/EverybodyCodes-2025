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

def isEven(num):
    if num % 2 == 0:
        return True
    
cnt = 0
for (tx,ty) in tList:
    if (tx+1,ty) in tList:
        cnt += 1
    if isEven(ty) and isEven(tx) and (tx,ty+1) in tList:
        cnt += 1
    if not isEven(ty) and not isEven(tx) and (tx,ty+1) in tList:
        cnt += 1
print(cnt)

'''
89

Your answer length is: incorrect
The first character of your answer is: incorrect
'''
 
