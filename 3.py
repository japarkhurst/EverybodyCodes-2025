input = '10,5,1,10,3,8,5,2,2'
boxes = [int(x) for x in input.split(',')]
print(sum(set(boxes)))

input = '4,51,13,64,57,51,82,57,16,88,89,48,32,49,49,2,84,65,49,43,9,13,2,3,75,72,63,48,61,14,40,77'
boxes = [int(x) for x in input.split(',')]
print(sum(sorted(set(boxes))[:20]))
print(max([boxes.count(x) for x in set(boxes)]))

countDict = {x:boxes.count(x) for x in set(boxes)}
#print(countDict)

for x in sorted(set(boxes),key=lambda x:countDict[x],reverse=True):
    print(f'{x}:{countDict[x]}')
