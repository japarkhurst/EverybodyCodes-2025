input = '''Vyrdax,Drakzyph,Fyrryn,Elarzris

R3,L2,R3,L1'''

input = '''Vyrdax,Drakzyph,Fyrryn,Elarzris

R3,L2,R3,L3'''

input = '''Lornvynar,Gaereldrith,Tirnoris,Wyrlar,Rysskael,Lornselor,Silmyr,Vyrllyr,Litheth,Karthath,Craggryph,Eaddin,Nyrixsaral,Xendjor,Paldpyr,Olardra,Elarselor,Raelnarith,Norakilor,Xyrfyr

L10,R9,L12,R14,L6,R11,L5,R7,L8,R7,L5,R14,L5,R12,L5,R8,L5,R9,L5,R14,L15,R12,L14,R9,L7,R12,L7,R15,L5'''

input = '''Gaeraris,Thazther,Aurepyxis,Ulkzris,Zraaldravor,Brelfyr,Vaelsaral,Valdax,Wynnixis,Glynnimar,Jaerthel,Rythtor,Nexxel,Wyrrovan,Ignlar,Vyrlsarix,Quirralis,Paldxaril,Zraalkyris,Maralsyx,Vornsaral,Vanagrath,Qalsin,Azkryth,Tororath,Gavidris,Glynnmal,Marlar,Orahmir,Lazvalir

L10,R15,L14,R19,L5,R29,L14,R39,L29,R32,L5,R22,L15,R16,L8,R32,L17,R49,L37,R39,L5,R27,L5,R26,L5,R24,L5,R37,L5,R35,L5,R9,L5,R11,L5,R29,L5,R33,L5,R30,L15,R48,L19,R34,L40,R28,L27,R10,L9,R48,L18,R36,L37,R15,L37,R21,L26,R46,L11'''


names, _, moves = input.split('\n')
names = names.split(',')
moves = moves.split(',')
name_count = len(names)
max_idx = name_count-1
cur_idx = 0
idx = 0
print(f'{name_count=}')
print(names)
for move in moves: 
    d = move[0]
    cnt = move[1:]
    cnt = int(cnt)
    print(f'{move=}, {cnt=}')
    cnt = cnt%name_count
    #while cnt>=name_count:
        #cnt-=name_count
    print(cnt)
    if d == 'L':
        cnt = -cnt
    idx += cnt
    print(idx)
    if idx < 0:
        # idx = 0
        idx = name_count + idx
    elif idx > max_idx:
        # idx = max_idx
        idx = idx - name_count
    print(f'{idx=}')
    #names[idx],names[cur_idx] = names[cur_idx],names[idx]
    cur,new = names[cur_idx],names[idx]
    print(cur,new)
    names[idx],names[cur_idx] = cur,new
    print(names)
    cur_idx = 0
    idx = 0
    
print(names[idx])
