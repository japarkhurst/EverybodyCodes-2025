input = '1,5,2,6,8,4,1,7,3'
nums = [int(x) for x in input.split(',')]
cnt = 8
crosses = sum([1 for i in range(len(nums)-1) if abs(nums[i]-nums[i+1]) == int(cnt/2)])
print(crosses)
