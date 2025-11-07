input = '''102
75
50
35
13'''

for i,x in enumerate(input.split('\n')):
    if i == 0:
        first = int(x)
last = int(x)
print(int(first/last*2025))

input = '''5
7|21
18|36
27|27
10|50
10|50
11'''

r = 1
for i,x in enumerate(input.split('\n')):
    if i == 0:
        r*=int(x)
    elif '|' in x:
        d,n = x.split('|')
        r*=(int(n)/int(d))
    else:
        r*=(1/int(x))
    #print(x,r)
print(int(r*100))
