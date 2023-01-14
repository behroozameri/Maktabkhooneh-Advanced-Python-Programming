def isAval(num):
    count = 0
    for i in range(2, (num // 2 + 1)):
        if num % i == 0:
            count += 1
    if count == 0:
        return 1
    else:
        return -1


inputLen = 10
inputList = []
for i in range(0,inputLen):
    inputList.append(int(input()))

maxInputNum = max(inputList)
avalList = dict()
for i in range(2,(maxInputNum // 2 + 1)):
    avalList[i] = isAval(i)

maxNum = -99999999999
maxCount = 0

for i in range(0,inputLen):
    count = 0
    for j in range(2,(inputList[i] // 2 + 1)):
        if avalList[j] == 1:
            if inputList[i] % j == 0:
                count += 1

    if count > maxCount :
        maxCount = count
        maxNum = inputList[i]
    elif count == maxCount:
        if inputList[i] > maxNum:
            maxNum = inputList[i]

print(maxNum, maxCount)
