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
pairDict = {}
for r in rules:
    start,ends = r.split(' > ')
    ends = ends.split(',')
    pairDict[start] = ends
    for end in ends:
        pairs.append(start+end)
print(pairDict)
keys = list(pairDict.keys())
name = names[0]
unique = {name}
for i in range(len(name)-1,11):
    print(i)
    subset = [x for x in unique if len(x)==i and x[-1] in keys]
    print(subset)
    for s in subset:
        options = pairDict[s[-1]]
        for opt in options:
            unique.add(s+opt)
unique = {u for u in unique if len(u) >= 7}
print(len(unique))            

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
