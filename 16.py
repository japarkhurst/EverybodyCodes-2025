input = '1,2,3,5,9'
nums = [int(x) for x in input.split(',')]
columns = 90
total = sum(int(columns//num) for num in nums)
print(total)
