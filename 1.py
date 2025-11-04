input = '''Vyrdax,Drakzyph,Fyrryn,Elarzris

R3,L2,R3,L1'''

names, _, moves = input.split('\n')
names = names.split(',')
moves = moves.split(',')
max_idx = len(names)-1
idx = 0
for move in moves: 
    d = move[0]
    cnt = move[1:]
    cnt = int(cnt)
    if d == 'L':
        cnt = -cnt
    idx += cnt
    if idx < 0:
        idx = 0
    elif idx > max_idx:
        idx = max_idx
print(names[idx])
