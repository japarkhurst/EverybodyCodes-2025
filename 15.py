input = 'R3,R4,L3,L4,R3,R6,R9'

L,R = 'L','R'
N,S,E,W = 'N','S','E','W'
walls = set((0,0))
cx,cy = (0,0)
face = N
L_Turn_Dict = {N:W,W:S,S:E,E:N}
R_Turn_Dict = {v:k for k,v in L_Turn_Dict.items()}
Move_Dict = {N:(0,1),W:(-1,0),S:(0,-1),E:(1,0)}
for inst in input.split(','):
    turn,cnt = inst[0],int(inst[1:])
    if turn == L:
        new_dir = L_Turn_Dict[face]
        dx,dy = Move_Dict[new_dir]
        for i in range(cnt):
            cx+=dx
            cy+=dy
            walls.add((cx,cy))
def printWalls(walls):
    xList = [w[0] for w in walls]
    yList = [w[1] for w in walls]
    row_count = max(yList) - min(yList)
    col_count = max(xList) - min(xList)
    for y in range(row_count):
        row = ''
        for x in range(col_count):
            if (x,y) in walls:
                row+='#'
            else:
                row+=' '
        print(row)
printWalls(walls)
                
    

