input = '''58:5,3,7,8,9,10,4,5,7,8,8'''

input = '''1:2,4,1,1,8,2,7,9,8,6
2:7,9,9,3,8,3,8,8,6,8
3:4,7,6,9,1,8,3,7,2,2
4:6,4,2,1,7,4,5,5,5,8
5:2,9,3,8,3,9,5,2,1,4
6:2,4,9,6,7,4,1,7,6,8
7:2,3,7,6,2,2,4,1,4,2
8:5,1,5,6,8,3,1,8,3,9
9:5,7,7,3,7,2,3,8,6,7
10:4,1,9,3,8,5,4,3,5,5'''

input = '''1:7,1,9,1,6,9,8,3,7,2
2:6,1,9,2,9,8,8,4,3,1
3:7,1,9,1,6,9,8,3,8,3
4:6,1,9,2,8,8,8,4,3,1
5:7,1,9,1,6,9,8,3,7,3
6:6,1,9,2,8,8,8,4,3,5
7:3,7,2,2,7,4,4,6,3,1
8:3,7,2,2,7,4,4,6,3,7
9:3,7,2,2,7,4,1,6,3,7'''

def parseLine(line):
    id,nums = line.split(':')
    return id,nums.split(',')
    
def calcFishbone(nums):
    l,m,r = 'l','m','r'
    fb = {}
    i = -1
    for n in nums:
        placed = False
        for i in range(len(fb)):
            if not fb[i][l] and int(n) < int(fb[i][m]):
                fb[i][l] = n
                placed = True
                break
            elif not fb[i][r] and int(n) > int(fb[i][m]):
                fb[i][r] = n
                placed = True
                break
        if not placed:
            fb[i+1] = {l:None,m:n,r:None}
    levels = []
    for i in range(len(fb)):
        seg_nums = [n for n in [fb[i][l],fb[i][m],fb[i][r]] if n]
        levels.append(int(''.join(seg_nums)))
    spine = ''.join([fb[i][m] for i in range(len(fb))])
    print(spine)
    return int(spine),levels

qualities = []
strengthDict = {}
for line in input.split('\n'):
    id,nums = parseLine(line)
    quality,levels = calcFishbone(nums)
    qualities.append(quality)
    strengthDict[id] = {'q':quality,'l':levels}
print(max(qualities)-min(qualities))
swordOrder = sorted(strengthDict,key=lambda x:[strengthDict[x]['q'],strengthDict[x]['l'],int(x)])[::-1]
print(swordOrder)

checksum = 0
for i,id in enumerate(swordOrder,1):
    checksum += (i*int(id))
print(checksum)
    
    


