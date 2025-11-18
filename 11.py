input = '''9
1
1
4
9
6'''

cols = [int(x) for x in input.split('\n')]
col_count = len(cols)
rounds = 10
phase = 1
move_made = False
target = int(sum(cols)/len(cols))
checksum = sum((idx*c for idx,c in enumerate(cols,1)))
print(f'0: {cols}: {checksum}')
for i in range(1,rounds+1):
    if phase == 1:
        for c in range(col_count-1):
            current_col = cols[c]
            next_col = cols[c+1]
            if current_col > next_col:
                cols[c]-=1
                cols[c+1]+=1
                move_made = True
        if not move_made:
            phase = 2
    if phase == 2:
        for c in range(col_count-1):
            current_col = cols[c]
            next_col = cols[c+1]
            if next_col > current_col:
                cols[c]+=1
                cols[c+1]-=1
    move_made = False
    checksum = sum((idx*c for idx,c in enumerate(cols,1)))
    #print(f'{phase}')
    print(f'{i}: {cols}: {checksum}')
    
    if len(set(cols)) == 1:
        print(f'Balanced after {i} rounds')
        break   
    
    
    
    
