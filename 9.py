input = '''1:CAAGCGCTAAGTTCGCTGGATGTGTGCCCGCG
2:CTTGAATTGGGCCGTTTACCTGGTTTAACCAT
3:CTAGCGCTGAGCTGGCTGCCTGGTTGACCGCG'''

input = '''1:GCAGGCGAGTATGATACCCGGCTAGCCACCCC
2:TCTCGCGAGGATATTACTGGGCCAGACCCCCC
3:GGTGGAACATTCGAAAGTTGCATAGGGTGGTG
4:GCTCGCGAGTATATTACCGAACCAGCCCCTCA
5:GCAGCTTAGTATGACCGCCAAATCGCGACTCA
6:AGTGGAACCTTGGATAGTCTCATATAGCGGCA
7:GGCGTAATAATCGGATGCTGCAGAGGCTGCTG'''

input = '''1:GCAGGCGAGTATGATACCCGGCTAGCCACCCC
2:TCTCGCGAGGATATTACTGGGCCAGACCCCCC
3:GGTGGAACATTCGAAAGTTGCATAGGGTGGTG
4:GCTCGCGAGTATATTACCGAACCAGCCCCTCA
5:GCAGCTTAGTATGACCGCCAAATCGCGACTCA
6:AGTGGAACCTTGGATAGTCTCATATAGCGGCA
7:GGCGTAATAATCGGATGCTGCAGAGGCTGCTG
8:GGCGTAAAGTATGGATGCTGGCTAGGCACCCG'''

dnaDict = {}
for row in input.split('\n'):
    id,dna = row.split(':')
    dnaDict[int(id)] = list(dna)

def calcDegree(c_dna,p1_id,p2_id):
    p1_dna = dnaDict[p1_id]
    p2_dna = dnaDict[p2_id]
    p1_degree = 0
    p2_degree = 0
    for i,c_char in enumerate(c_dna):
        p1_char = p1_dna[i]
        p2_char = p2_dna[i]
        if c_char not in (p1_char,p2_char):
            p1_degree, p2_degree = 0,0
            break
        if c_char == p1_char:
            p1_degree+=1
        if c_char == p2_char:
            p2_degree+=1
    return p1_degree * p2_degree

cnt = len(dnaDict)
masterDegreeDict = {}
childParentDict = {}
for c_id,c_dna in dnaDict.items():
    #parents = [id for id in dnaDict if id != c_id]
    #p1_id,p2_id = parents
    degreeDict = {}
    degreeFound = False
    for p1_id in range(1,cnt+1):
        for p2_id in range(1,cnt+1):
            if (p2_id,p1_id) in degreeDict or p1_id == p2_id or p1_id == c_id or p2_id == c_id:
                continue
            degree = calcDegree(c_dna,p1_id,p2_id)
            if not degree:
                continue
            degreeFound = True
            degreeDict[(p1_id,p2_id)] = degree
            childParentDict[c_id] = (p1_id,p2_id)
            break
        if degreeFound:
            break
    if not degreeDict:
        continue
    masterDegreeDict[c_id] = {k:v for k,v in degreeDict.items() if v}
#print(masterDegreeDict)
totalDegrees = 0
for c_id,degree_dict in masterDegreeDict.items():
    degrees = sum(degree_dict.values())
    totalDegrees+=degrees
print(totalDegrees)

'''
cnt = len(dnaDict)
degreeDict = {}
childParentDict = {}
parents = set()
children = set()
for c_id,c_dna in dnaDict.items():
    #print(c_id)
    if c_id in parents:
        continue
    degree = 0
    for p1_id in range(1,cnt+1):
        for p2_id in range(1,cnt+1):
            if p1_id == p2_id or p1_id == c_id or p2_id == c_id:
                #print(f'First Exit: {c_id}: {p1_id},{p2_id}')
                continue
            #elif p1_id in children or p2_id in children:
                #print(f'Second Exit: {c_id}: {p1_id},{p2_id}')
                #continue
            degree = calcDegree(c_dna,p1_id,p2_id)
            #print(f'{c_id}: {p1_id},{p2_id}: {degree}')
            if not degree:
                continue
            childParentDict[c_id] = (p1_id,p2_id)
            parents.add(p1_id)
            parents.add(p2_id)
            break
        if degree:
            break
    if not degree:
        continue
    degreeDict[c_id] = degree
    children.add(c_id)
#print(children)
#print(parents)
#print(childParentDict)
#print(degreeDict)
totalDegrees = sum({v for k,v in degreeDict.items()})
print(totalDegrees)
'''

families = []
for c_id,(p1_id,p2_id) in childParentDict.items():
    f_indices = [i for i,f in enumerate(families) if p1_id in f or p2_id in f]
    #print(f_indices)
    if f_indices:
        new_family = set()
        families_to_remove = []
        for f_index in f_indices:
            family = families[f_index]
            #print(family)
            new_family.update(family)
            families_to_remove.append(family)
        new_family.update({c_id,p1_id,p2_id})
        families.append(new_family)
        for family in families_to_remove:
            families.remove(family)
        
    else:
        families.append({c_id,p1_id,p2_id})
#print(families)
print(sum(max(families,key=lambda x:len(x))))


'''
12243
Your answer length is: correct
The first character of your answer is: incorrect

17523
Your answer length is: correct
The first character of your answer is: incorrect
'''
