inputLen = int(input())
myList = []
for i in range(0, inputLen):
    inputString = input()
    tmp = inputString.split('.')
    tmp[1] = tmp[1][0].upper() + tmp[1][1:].lower()
    myList.append(tmp)

for i in range(0, inputLen):
    for j in range(0, inputLen):
        if myList[i][0] < myList[j][0]:
            myList[i],myList[j] = myList[j],myList[i]
        elif myList[i][0] == myList[j][0]:
            if myList[i][1] < myList[j][1]:
                myList[i],myList[j] = myList[j],myList[i]

for i in range(0, inputLen):
    print(myList[i][0], myList[i][1], myList[i][2])
