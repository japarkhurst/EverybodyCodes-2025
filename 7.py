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

names,rules = input.split("\n\n")
names = names.split(',')
rules = rules.split('\n')

pairs = []
for r in rules:
    start,ends = r.split(' > ')
    for end in ends:
        pairs.append(start+end)
#print(pairs)

found = False
invalid = False
for name in names:
    for i in range(len(name)-1):
        test = name[i:i+2]
        if test not in pairs:
            invalid = True
            break
    if not invalid:
        break
print(name)
            
