input = '''Vyrdax,Drakzyph,Fyrryn,Elarzris

R3,L2,R3,L1'''

names, _, moves = input.split('\n')
names = names.split(',')
moves = moves.split(',')
name_count = len(names)
max_idx = name_count-1
idx = 0
for move in moves: 
    d = move[0]
    cnt = move[1:]
    cnt = int(cnt)
    if d == 'L':
        cnt = -cnt
    cnt = cnt%name_count
    idx += cnt
    
    if idx < 0:
        # idx = 0
        idx = name_count + cnt
    elif idx > max_idx:
        # idx = max_idx
        idx = cnt - name_count
print(names[idx])

# not Craggryph
