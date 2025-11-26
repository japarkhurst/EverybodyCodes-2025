input = '''189482189843433862719
279415473483436249988
432746714658787816631
428219317375373724944
938163982835287292238
627369424372196193484
539825864246487765271
517475755641128575965
685934212385479112825
815992793826881115341
1737798467@7983146242
867597735651751839244
868364647534879928345
519348954366296559425
134425275832833829382
764324337429656245499
654662236199275446914
317179356373398118618
542673939694417586329
987342622289291613318
971977649141188759131'''

input = '''4547488458944
9786999467759
6969499575989
7775645848998
6659696497857
5569777444746
968586@767979
6476956899989
5659745697598
6874989897744
6479994574886
6694118785585
9568991647449'''

rows = input.split('\n')
rowCount = len(rows)
colCount = len(rows[0])
R = 10
charDict = {}
for y,row in enumerate(rows):
    for x,char in enumerate(row):
        if char == '@':
            V = (x,y)
        else:
            charDict[(x,y)] = int(char)
Xv,Yv = V
result = sum(num for (Xc,Yc),num in charDict.items() if (Xv - Xc) * (Xv - Xc) + (Yv - Yc) * (Yv - Yc) <= R * R)
print(result)

R = max(rowCount,colCount)
burnDict = {}
priorBurned = 0
for i in range(1,R+1):
    burned = sum(num for (Xc,Yc),num in charDict.items() if (Xv - Xc) * (Xv - Xc) + (Yv - Yc) * (Yv - Yc) <= i * i)
    burnDict[i] = burned-priorBurned
    priorBurned=burned
print(burnDict)
maxBurnRound = max(burnDict,key=lambda x:burnDict[x])
result = maxBurnRound * burnDict[maxBurnRound]
print(result)
#R:1   Lava:26          R:2   Lava:49          R:3  Lava:109 
#R:4  Lava:146          R:5  Lava:218          R:6  Lava:199

#4150
#Your answer length is: incorrect
#The first character of your answer is: incorrect
