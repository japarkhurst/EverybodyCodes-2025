input = '''Plant 1 with thickness 1:
- free branch with thickness 1

Plant 2 with thickness 1:
- free branch with thickness 1

Plant 3 with thickness 1:
- free branch with thickness 1

Plant 4 with thickness 17:
- branch to Plant 1 with thickness 15
- branch to Plant 2 with thickness 3

Plant 5 with thickness 24:
- branch to Plant 2 with thickness 11
- branch to Plant 3 with thickness 13

Plant 6 with thickness 15:
- branch to Plant 3 with thickness 14

Plant 7 with thickness 10:
- branch to Plant 4 with thickness 15
- branch to Plant 5 with thickness 21
- branch to Plant 6 with thickness 34'''

from dataclasses import dataclass

@dataclass
class Branch():
    source: int
    to: int
    thickness: int
    
@dataclass
class Plant():
    id: int
    thickness: int
    energy: int = 0
    branches: list[Branch] = None
    
plants = []
branches = []
for row in input.split('\n'):
    if row.startswith('Plant'):
        _,id,_,_,thickness = row.strip(':').split(' ')
        pid = int(id)
        p = Plant(id=pid,thickness=int(thickness))
    elif '-' in row:
        if 'free' in row:
            to_id = 0
            thickness = 1
        else:
            _,_,_,_,to_id,_,_,thickness = row.split(' ')
        b = Branch(source=pid,to=int(to_id),thickness=int(thickness))
        branches.append(b)
    else:
        p.branches = branches
        plants.append(p)
        branches = []
p.branches = branches
plants.append(p)
branches = []
pDict = {p.id:p for p in plants}
for i in range(1,len(plants)):
    p = pDict[i]
    incoming = 0
    for b in p.branches:
        if b.to:
            to_energy = pDict[b.to].energy * b.thickness
        else:
            to_energy  = 1
        incoming += to_energy
    print(f'incoming for {i}: {incoming}')
    if incoming >= p.thickness:
        pDict[i].energy = incoming
    else:
        pDict[i].energy = 0
print(incoming)
