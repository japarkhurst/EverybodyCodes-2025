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
for c_id,c_dna in dnaDict.items():
    #parents = [id for id in dnaDict if id != c_id]
    #p1_id,p2_id = parents
    degreeDict = {}
    for p1_id in range(1,cnt+1):
        for p2_id in range(1,cnt+1):
            if (p2_id,p1_id) in degreeDict or p1_id == p2_id or p1_id == c_id or p2_id == c_id:
                continue
            degree = calcDegree(c_dna,p1_id,p2_id)
            if not degree:
                continue
            degreeDict[(p1_id,p2_id)] = degree
    if not degreeDict:
        continue
    masterDegreeDict[c_id] = {k:v for k,v in degreeDict.items() if v}
print(masterDegreeDict)
totalDegrees = 0
for c_id,degree_dict in masterDegreeDict.items():
    degrees = sum(degree_dict.values())
    totalDegrees+=degrees
print(totalDegrees)
    
        
