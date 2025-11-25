input = '1,2,3,5,9'
nums = [int(x) for x in input.split(',')]
columns = 90
total = sum(int(columns//num) for num in nums)
print(total)

input = '1,2,2,2,2,3,1,2,3,3,1,3,1,2,3,2,1,4,1,3,2,2,1,3,2,2'
wall = [int(x) for x in input.split(',')]
wallLength = len(wall)
spell = []
total = 1
idx = 0
while sum(wall) > 0:
    idx+=1
    idxList = [i for i,x in enumerate(wall) if (i+1)%idx == 0]
    valid = all(wall[i] >= 1 for i in idxList)
    if not valid:
        continue
    for i in idxList:
        wall[i]-=1
    total*=idx
    spell.append(idx)
print(total)
print(spell)

spell = '1,2,2,2,2,3,1,2,3,3,1,3,1,2,3,2,1,4,1,3,2,2,1,3,2,2'
#spell = '1,2,4,8,12,38,66,72,98,120,122,136,154,156,163,183,202,205,218,237,248,262,269,292,300,461,601,733,887,953'
wall = [int(x) for x in spall.split(',')
        
target = 202520252025000
length = 94439495762954 
target = 1000
max_i = 1000
i = 0
while True and i < max_i:
    i+=1
    
