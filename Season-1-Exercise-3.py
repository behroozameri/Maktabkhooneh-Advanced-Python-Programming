filmType = dict()
filmType['Action'] = 0
filmType['Adventure'] = 0
filmType['History'] = 0
filmType['Comedy'] = 0
filmType['Romance'] = 0
filmType['Horror'] = 0

inputLen = int(input())
for i in range(0, inputLen):
    inputString = input()
    tmp = inputString.split(' ')
    for j in range(1,len(tmp)):
        filmType[tmp[j]] += 1

filmList = []
for key, value in filmType.items():
    tmp = []
    tmp.append(key)
    tmp.append(value)
    filmList.append(tmp)

for i in range(0, len(filmList)):
    for j in range(0, len(filmList)):
        if filmList[i][1] > filmList[j][1]:
            filmList[i], filmList[j] = filmList[j], filmList[i]
        elif filmList[i][1] == filmList[j][1]:
            if filmList[i][0] < filmList[j][0]:
                filmList[i], filmList[j] = filmList[j], filmList[i]

for i in range(0, len(filmList)):
    print(filmList[i][0], ':', filmList[i][1])
