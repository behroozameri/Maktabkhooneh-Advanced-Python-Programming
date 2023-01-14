def getResult():
    result = input()
    tmp = result.split('-')
    team_A = int(tmp[0])
    team_B = int(tmp[1])
    return team_A, team_B

Spain = [0,0,0,0,0]
Iran = [0,0,0,0,0]
Portugal = [0,0,0,0,0]
Morocco = [0,0,0,0,0]

result_A, result_B = getResult()
goalDiff_A = result_A - result_B
goalDiff_B = result_B - result_A
if result_A > result_B:
    Iran[0] += 1
    Spain[1] += 1
    Iran[4] += 3
    Iran[3] += goalDiff_A
    Spain[3] += goalDiff_B
elif result_A < result_B:
    Iran[1] += 1
    Spain[0] += 1
    Spain[4] += 3
    Iran[3] += goalDiff_A
    Spain[3] += goalDiff_B
else:
    Iran[2] += 1
    Spain[2] += 1
    Iran[4] += 1
    Spain[4] += 1

result_A, result_B = getResult()
goalDiff_A = result_A - result_B
goalDiff_B = result_B - result_A
if result_A > result_B:
    Iran[0] += 1
    Portugal[1] += 1
    Iran[4] += 3
    Iran[3] += goalDiff_A
    Portugal[3] += goalDiff_B
elif result_A < result_B:
    Iran[1] += 1
    Portugal[0] += 1
    Portugal[4] += 3
    Iran[3] += goalDiff_A
    Portugal[3] += goalDiff_B
else:
    Iran[2] += 1
    Portugal[2] += 1
    Iran[4] += 1
    Portugal[4] += 1

result_A, result_B = getResult()
goalDiff_A = result_A - result_B
goalDiff_B = result_B - result_A
if result_A > result_B:
    Iran[0] += 1
    Morocco[1] += 1
    Iran[4] += 3
    Iran[3] += goalDiff_A
    Morocco[3] += goalDiff_B
elif result_A < result_B:
    Iran[1] += 1
    Morocco[0] += 1
    Morocco[4] += 3
    Iran[3] += goalDiff_A
    Morocco[3] += goalDiff_B
else:
    Iran[2] += 1
    Morocco[2] += 1
    Iran[4] += 1
    Morocco[4] += 1

result_A, result_B = getResult()
goalDiff_A = result_A - result_B
goalDiff_B = result_B - result_A
if result_A > result_B:
    Spain[0] += 1
    Portugal[1] += 1
    Spain[4] += 3
    Spain[3] += goalDiff_A
    Portugal[3] += goalDiff_B
elif result_A < result_B:
    Spain[1] += 1
    Portugal[0] += 1
    Portugal[4] += 3
    Spain[3] += goalDiff_A
    Portugal[3] += goalDiff_B
else:
    Spain[2] += 1
    Portugal[2] += 1
    Spain[4] += 1
    Portugal[4] += 1

result_A, result_B = getResult()
goalDiff_A = result_A - result_B
goalDiff_B = result_B - result_A
if result_A > result_B:
    Spain[0] += 1
    Morocco[1] += 1
    Spain[4] += 3
    Spain[3] += goalDiff_A
    Morocco[3] += goalDiff_B
elif result_A < result_B:
    Spain[1] += 1
    Morocco[0] += 1
    Morocco[4] += 3
    Spain[3] += goalDiff_A
    Morocco[3] += goalDiff_B
else:
    Spain[2] += 1
    Morocco[2] += 1
    Spain[4] += 1
    Morocco[4] += 1

result_A, result_B = getResult()
goalDiff_A = result_A - result_B
goalDiff_B = result_B - result_A
if result_A > result_B:
    Portugal[0] += 1
    Morocco[1] += 1
    Portugal[4] += 3
    Portugal[3] += goalDiff_A
    Morocco[3] += goalDiff_B
elif result_A < result_B:
    Portugal[1] += 1
    Morocco[0] += 1
    Morocco[4] += 3
    Portugal[3] += goalDiff_A
    Morocco[3] += goalDiff_B
else:
    Portugal[2] += 1
    Morocco[2] += 1
    Portugal[4] += 1
    Morocco[4] += 1

teamTable = []
Iran.append('Iran')
teamTable.append(Iran)
Spain.append('Spain')
teamTable.append(Spain)
Portugal.append('Portugal')
teamTable.append(Portugal)
Morocco.append('Morocco')
teamTable.append(Morocco)

for i in range(0,len(teamTable)):
    for j in range(0,len(teamTable)):
        if teamTable[i][4] > teamTable[j][4]:
            teamTable[i],teamTable[j] = teamTable[j],teamTable[i]
        elif teamTable[i][4] == teamTable[j][4]:
            if teamTable[i][0] > teamTable[j][0]:
                teamTable[i],teamTable[j] = teamTable[j],teamTable[i]
            elif teamTable[i][0] == teamTable[j][0]:
                if teamTable[i][5] < teamTable[j][5]:
                    teamTable[i],teamTable[j] = teamTable[j],teamTable[i]

for i in range(0,len(teamTable)):
    print('%s  wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i'  %(teamTable[i][5], teamTable[i][0], teamTable[i][1], teamTable[i][2], teamTable[i][3], teamTable[i][4]))
