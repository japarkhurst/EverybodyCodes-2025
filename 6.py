input = 'ABabACacBCbca'
m = 0
cnt = 0
for x in input:
    if x == 'A':
        m+=1
    elif x == 'a':
        cnt += m
print(cnt)

input = 'ABabACacBCbca'
cnt = 0
for l in ('a','b','c'):
    m = 0
    subset = [x for x in input if x.lower() == l]
    for x in input:
        if x == l.upper():
            m+=1
        elif x == l:
            cnt += m
print(cnt)

input = 'AABCBABCABCabcabcABCCBAACBCa'
cnt = 0
multiplier = 1
distance = 10
input *= multiplier
length = len(input)
for idx,l in enumerate(input):
    if l.isupper():
        continue
    min_idx = max(idx-distance,0)
    max_idx = min(idx+distance,length)
    subset = [x for x in input[min_idx:max_idx+1]]
    print("".join(subset))
    subset_cnt = len([x for x in subset if x == l.upper()])
    print(subset_cnt)
    cnt += subset_cnt
print(cnt)

input = 'AABCBABCABCabcabcABCCBAACBCa'
cnt = 0
multiplier = 1000
distance = 1000
#input *= multiplier
init_length = len(input)
print(f'{init_length=}')
num_needed_for_repeat = distance//init_length + 1
input_iterations = num_needed_for_repeat * 3 # one for start, one for middle, one for end
repeat_multiplier = multiplier - (num_needed_for_repeat*2) # number of times to multiply the middle section
start_mid_break = num_needed_for_repeat * init_length
mid_end_break = start_mid_break * 2
print(f'{num_needed_for_repeat=}\n{input_iterations=}\n{repeat_multiplier=}\n{start_mid_break=}\n{mid_end_break=}')
input *= input_iterations
length = len(input)
print(f'{length=}')
start,mid,end = 0,0,0
start_cnt, mid_cnt, end_cnt = 0,0,0
for idx,l in enumerate(input):
    if l.isupper():
        continue
    min_idx = max(idx-distance,0)
    max_idx = min(idx+distance,length)
    subset = [x for x in input[min_idx:max_idx+1]]
    #print("".join(subset))
    subset_cnt = len([x for x in subset if x == l.upper()])
    #print(subset_cnt)
    if idx < start_mid_break:
        start+=subset_cnt
        start_cnt+=1
    elif idx >= mid_end_break:
        end+=subset_cnt
        end_cnt+=1
    else:
        mid+=subset_cnt
        mid_cnt+=1
    #cnt += subset_cnt
print(f'{start_cnt=},{mid_cnt=},{end_cnt=}')
print(f'{start=},{mid=},{end=}')
cnt = start + mid*(repeat_multiplier) + end
print(cnt)
