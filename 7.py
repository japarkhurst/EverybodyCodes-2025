input = '''Khara,Xaryt,Noxer,Kharax

r > v,e,a,g,y
a > e,v,x,r,g
e > r,x,v,t
h > a,e,v
g > r,y
y > p,t
i > v,r
K > h
v > e
B > r
t > h
N > e
p > h
H > e
l > t
z > e
X > a
n > v
x > z
T > i'''

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
#print(pairDict)


found = False
invalid = False
invalidList = []
for name in names:
    for i in range(len(name)-1):
        test = name[i:i+2]
        if test not in pairs:
            #print(f'{name}: {test}')
            invalid = True
            invalidList.append(name)
            break
validNames = [x for x in names if x not in invalidList]
print(validNames)
indices = [i for i,x in enumerate(names) if x in validNames]
print(sum(indices))

keys = list(pairDict.keys())
names = validNames
unique = set(names)
for name in names:
    for i in range(len(name)-1,11):
        #print(i)
        subset = [x for x in unique if len(x)==i and x[-1] in keys]
        #print(subset)
        for s in subset:
            options = pairDict[s[-1]]
            for opt in options:
                unique.add(s+opt)
unique = {u for u in unique if len(u) >= 7 and len(u)<=11}
print(len(unique))            
