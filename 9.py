input = '''1:CAAGCGCTAAGTTCGCTGGATGTGTGCCCGCG
2:CTTGAATTGGGCCGTTTACCTGGTTTAACCAT
3:CTAGCGCTGAGCTGGCTGCCTGGTTGACCGCG'''

dnaDict = {}
for row in input.split('\n'):
    id,dna = row.split(':')
    dnaDict[id] = list(dna)

degreeDict = {}
for c_id,c_dna in dnaDict.items():
    invalid = False
    parents = [id for id in dnaDict if id != c_id]
    p1,p2 = parents
    p1_dna = dnaDict[p1]
    p2_dna = dnaDict[p2]
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
    degreeDict[c_id] = p1_degree * p2_degree
print(degreeDict)
        
