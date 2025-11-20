input = '''72
58
47
61
67'''

nums = [int(x) for x in input.split('\n')]
num_count = len(nums)
length = num_count + 1

half1 = [x for i,x in enumerate(nums) if i%2 == 0]
half2 = [x for i,x in enumerate(nums) if i%2 != 0][::-1]

dial = [1] + half1 + half2
#print(dial)

clicks = 2025%length
#print(clicks)
print(dial[clicks])



input = '''10-15
12-13
20-21
19-23
30-37'''

half1 = []
half2 = []
ranges = input.split('\n')
for i,r in enumerate(ranges):
    start,end = r.split('-')
    start,end = int(start),int(end)
    if i%2 == 0:
        half1+=list(range(start,end+1))
    else:
        half2+=list(range(start,end+1))
        
dial = [1] + half1 + half2[::-1]
#print(dial)

clicks = 20252025%len(dial)
#print(clicks)
print(dial[clicks])



half1 = []
half2 = []
ranges = input.split('\n')
for i,r in enumerate(ranges):
    start,end = r.split('-')
    start,end = int(start),int(end)
    if i%2 == 0:
        half1.append((start,end))
    else:
        half2.append((end,start))
        
dial = [(1,1)] + half1 + half2[::-1]
#print(dial)

dialIdx = []
idx = -1
for start,end in dial:
    startIdx = idx+1
    endIdx = abs(end-start)+startIdx
    idx = endIdx
    dialIdx.append((startIdx,endIdx))
#print(dialIdx)

#print(endIdx)
clicks = 20252025%(endIdx+1)
#print(clicks)

idxNumDict = dict(zip(dialIdx,dial))
#print(idxNumDict)

for startIdx,endIdx in dialIdx:
    if startIdx <= clicks <= endIdx:
        start,end = idxNumDict[(startIdx,endIdx)]
        #print(f'{start},{end}')
        subclicks = clicks-startIdx
        #print(subclicks)
        if start > end:
            result = start - subclicks
        else:
            result = start + subclicks
print(result)        

