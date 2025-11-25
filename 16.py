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
spell = '1,2,3,5,9'
#spell = '1,2,4,8,12,38,66,72,98,120,122,136,154,156,163,183,202,205,218,237,248,262,269,292,300,461,601,733,887,953'

spell = [int(x) for x in spell.split(',')]
        
target = 202520252025000
length = 94439495762954 
target = 1000
max_i = 100
maxBound = target
minBound = 0
i = 0
while True and i < max_i:
    i+=1
    #maxBlocks = sum(int(maxBound//num) for num in wall)
    #minBlocks = sum(int(minBound//num) for num in wall)
    guessedLength = maxBound - int((maxBound-minBound)//2)
    print(f'Searching for {guessedLength} between {minBound} and {maxBound}')
    blocksRequired = sum(int(guessedLength//num) for num in spell)
    print(f'{guessedLength} as guessed length uses {blocksRequired}')
    if blocksRequired == target:
        print(f'Target found exactly using {blocksRequired} and length {guessedLength}')
        break
    elif blocksRequired < target:
        print(f'Block count {blocksRequired} less than target using {guessedLength} length')
        minBound = guessedLength
    elif blocksRequired > target:
        print(f'Block count {blocksRequired} greater than target using {guessedLength} length')
        maxBound = guessedLength
    if maxBound - minBound == 1:
        print(f'Target found between {maxBound} and {minBound}; choosing {minBound}')
        break
print(minBound)  
'''
blocks     the length of the wall
               1                          1
              10                          5
             100                         47
            1000                        467
           10000                       4664
          100000                      46633
         1000000                     466322
        10000000                    4663213
       100000000                   46632125
      1000000000                  466321244
     10000000000                 4663212435
    100000000000                46632124353
   1000000000000               466321243524
  10000000000000              4663212435233
 100000000000000             46632124352332
 202520252025000             94439495762954
 '''
    
