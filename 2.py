

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

R = [0,0]
A = [25,9]
for I in range(3):
    R = multiply(R,R)
    print(R)
    R = divide(R,(10,10))
    print(R)
    R = add(R,A)
    print(R)

Cycle I
R = R * R = [0,0]
R = R / [10,10] = [0,0]
R = R + A = [25,9]

