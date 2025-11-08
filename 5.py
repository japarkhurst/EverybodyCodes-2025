input = '''58:5,3,7,8,9,10,4,5,7,8,8'''

def parseLine(line):
    id,nums = line.split(':')
    return id,nums.split(',')
    
def calcQuality(nums):
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
    spine = ''.join([fb[i][m] for i in range(len(fb))])
    print(spine)
    return int(spine)

qualities = []
for line in input.split('\n'):
    id,nums = parseLine(line)
    quality = calcQuality(nums)
    qualities.append(quality)
print(max(qualities)-min(qualities))
    
