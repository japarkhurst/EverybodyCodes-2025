input = '''Vyrdax,Drakzyph,Fyrryn,Elarzris

R3,L2,R3,L1'''

input = '''Lornvynar,Gaereldrith,Tirnoris,Wyrlar,Rysskael,Lornselor,Silmyr,Vyrllyr,Litheth,Karthath,Craggryph,Eaddin,Nyrixsaral,Xendjor,Paldpyr,Olardra,Elarselor,Raelnarith,Norakilor,Xyrfyr

L10,R9,L12,R14,L6,R11,L5,R7,L8,R7,L5,R14,L5,R12,L5,R8,L5,R9,L5,R14,L15,R12,L14,R9,L7,R12,L7,R15,L5'''
names, _, moves = input.split('\n')
names = names.split(',')
moves = moves.split(',')
name_count = len(names)
max_idx = name_count-1
idx = 0
print(f'{name_count=}')
for move in moves: 
    d = move[0]
    cnt = move[1:]
    cnt = int(cnt)
    print(f'{move=}, {cnt=}')
    cnt = cnt%name_count
    print(cnt)
    if d == 'L':
        cnt = -cnt
    idx += cnt
    print(idx)
    if idx < 0:
        # idx = 0
        idx += name_count
    elif idx > max_idx:
        # idx = max_idx
        idx -= name_count
    print(f'{idx=}')
print(names[idx])
