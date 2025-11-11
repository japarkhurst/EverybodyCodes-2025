input = 'ABabACacBCbca'

m = 0
cnt = 0
for x in input:
    if x == 'A':
        m+=1
    elif x == 'a':
        cnt += m
print(cnt)
