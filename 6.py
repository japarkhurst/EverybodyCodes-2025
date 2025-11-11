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
#input = 'ABCBABBCbbaACaACbCBbBbacBBccaAbbabCcbacAbAAACbaaACAbbbBaCBBBAccbbBaBCBAaBaCAcBcBaAAcCCCaAcbbAaCBabaA'
input = 'ABCAbbCBAaabCAbBcBbcBCbabBCBACcCbAAcabcbCACcacBbBbBbaAcbbBCccbbBcaCCcAabABBcbBAAccabAaCcCCcCcaaCCaaAbAbcAaaAAbBbcaaAAaABaAACaCAaBabBACacCccBCcacBcccACcCaBCBbaCBabCBaACbAaABAbcCaAbcbABBbBbcabbCBbBbcBAACaABAbcCaAbbaCaAAcBCAACbBAaABBAaBacBAABACBcaccCbaBCcBcACbcBAbcCACaCbaabbBaaAAbbaAaCBBCCCaaccCAaCcBcb'
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
