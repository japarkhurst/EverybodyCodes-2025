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
        n,d = x.split('|')
        r*=(int(n)/int(d))
    else:
        r*=(1/int(x))
    print(r)
print(r*100)
