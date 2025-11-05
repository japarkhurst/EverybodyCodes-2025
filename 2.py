def multiply(R1,R2):
    X1,Y1 = R1
    X2,Y2 = R2
    return (X1 * X2 - Y1 * Y2, X1 * Y2 + Y1 * X2)

def add(R1,R2):
    X1,Y1 = R1
    X2,Y2 = R2
    return (X1 + X2, Y1 + Y2)

def divide(R1,R2):
    X1,Y1 = R1
    X2,Y2 = R2
    return (X1 // X2, Y1 // Y2)

def cycle(R,A,divisor):
    R = multiply(R,R)
    R = divide(R,divisor)
    R = add(R,A)
    return R

A = [25,9]
R = [0,0]
for i in range(3):
    R = cycle(R,A,(10,10))
print(R)

A=[35300,-64910]
Z = add(A,(1000,1000))
print(A,Z)

ax,ay = A
zx,zy = Z
stepX = (zx-ax)//100
stepY = (zy-ay)//100
print(stepX,stepY)
xCoords = list(range(ax,zx+1,stepX))
yCoords = list(range(ay,zy+1,stepY))
print(len(xCoords))
pts = list(zip(xCoords, yCoords))
pts = []
for x in xCoords:
    for y in yCoords:
        pts.append((x,y))
print(pts[:5])
print(pts[-5:])
print(len(pts))

engraved_cnt = 0
for pt in pts:
    R = (0,0)
    engraved = True
    for i in range(100):
        R = cycle(R,pt,(100000,100000))
        if abs(R[0])>1000000 or abs(R[1])>1000000:
            engraved = False
            break
    if engraved:
        engraved_cnt+=1
print(engraved_cnt)