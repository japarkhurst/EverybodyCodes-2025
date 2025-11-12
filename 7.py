input = '''Oronris,Urakris,Oroneth,Uraketh

r > a,i,o
i > p,w
n > e,r
o > n,m
k > f,r
a > k
U > r
e > t
O > r
t > h'''

input = '''Harkris,Hazkris,Harox,Hazox,Kykris,Kyox,Kyagrath,Hazagrath,Haragrath

K > y
H > a
r > a,i,o,k
t > h
z > a,o,k
o > x
y > a,b
g > r
a > g,t,b
k > r
i > s'''

names,rules = input.split("\n\n")
names = names.split(',')
rules = rules.split('\n')

pairs = []
for r in rules:
    start,ends = r.split(' > ')
    ends = ends.split(',')
    for end in ends:
        pairs.append(start+end)
print(pairs)

found = False
invalid = False
invalidList = []
for name in names:
    for i in range(len(name)-1):
        test = name[i:i+2]
        if test not in pairs:
            print(f'{name}: {test}')
            invalid = True
            invalidList.append(name)
            break
    if not invalid:
        break
print(name)
print([x for x in names if x not in invalidList])
indices = [i for i,x in enumerate(names,1) if x not in invalidList]
print(indices)
print(sum(indices))
