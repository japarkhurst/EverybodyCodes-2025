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
