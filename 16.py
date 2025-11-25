input = '1,2,3,5,9'
nums = [int(x) for x in input.split(',')]
columns = 90
total = sum(int(columns//num) for num in nums)
print(total)

input = '1,2,2,2,2,3,1,2,3,3,1,3,1,2,3,2,1,4,1,3,2,2,1,3,2,2'
wall = [int(x) for x in input.split(',')]
wallLength = len(wall)
nums = []
idx = 0
while sum(wall) > 0:
    idx+=1
    idxList = [i for i,x in enumerate(wall) if wallLength%i == 0]
    valid = all(wall[i] >= 1 for i in idxList)
    if not valid:
        continue
    for i in idxList:
        wall[i]-=1
    nums.append(idx)

    
    
