input = 'R3,R4,L3,L4,R3,R6,R9'
input = 'L6,L3,L6,R3,L6,L3,L3,R6,L6,R6,L6,L6,R3,L3,L3,R3,R3,L6,L6,L3'
L,R = 'L','R'
N,S,E,W = 'N','S','E','W'
walls = []
cx,cy = (0,0)
walls.append((cx,cy))
face = N
L_Turn_Dict = {N:W,W:S,S:E,E:N}
R_Turn_Dict = {v:k for k,v in L_Turn_Dict.items()}
Move_Dict = {N:(0,1),W:(-1,0),S:(0,-1),E:(1,0)}
for inst in input.split(','):
    turn,cnt = inst[0],int(inst[1:])
    #print(f'Moving {cnt} to the {turn}')
    if turn == L:
        new_dir = L_Turn_Dict[face]
    else:
        new_dir = R_Turn_Dict[face]
    #print(f'Turning from {face} to {new_dir}')
    dx,dy = Move_Dict[new_dir]
    #print(f'Move x {dx}, y {dy}')
    for i in range(cnt):
        cx+=dx
        cy+=dy
        walls.append((cx,cy))
        #print(f'Adding ({cx},{cy})')
    face = new_dir
def printWalls(walls):
    xList = sorted({w[0] for w in walls})
    yList = sorted({w[1] for w in walls})
    start,end = walls[0],walls[-1]
    for y in range(max(yList),min(yList)-1,-1):
        row = ''
        for x in range(min(xList),max(xList)+1):
            if (x,y) == start:
                row+='S'
            elif (x,y) == end:
                row+='E'
            elif (x,y) in walls:
                row+='#'
            else:
                row+=' '
        print(row)
#print(sorted(walls))
printWalls(walls)
                
    
