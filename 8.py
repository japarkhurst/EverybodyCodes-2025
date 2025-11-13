input = '1,5,2,6,8,4,1,7,3'
nums = [int(x) for x in input.split(',')]
cnt = 8
crosses = sum([1 for i in range(len(nums)-1) if abs(nums[i]-nums[i+1]) == int(cnt/2)])
print(crosses)


input = '1,5,2,6,8,4,1,7,3,5,7,8,2'
nums = [int(x) for x in input.split(',')]
cnt = 8
pairs = [sorted((nums[i],nums[i+1])) for i in range(len(nums)-1)]
print(pairs)
strung = []
knots = 0
for s,e in pairs:
    cnt = sum(1 for s1,e1 in strung if (s<s1<e and (e1<s or e1>e)) or (s<e1<e and (s1<s or s1>e)))
    print(cnt)
    knots += cnt
    strung.append((s,e))
print(knots)


