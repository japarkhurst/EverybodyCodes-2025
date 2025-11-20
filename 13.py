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
