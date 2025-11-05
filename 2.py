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

def cycle(R,divisor):
    R = multiply(R,R)
    R = divide(R,divisor)
    R = add(R,A)
    return R

A = [25,9]
R = [0,0]
for i in range(3):
    R = cycle(R,(10,10))
print(R)
