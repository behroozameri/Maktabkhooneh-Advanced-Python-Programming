inputString = input()
words = inputString.split(' ')
myWords = []
if words[1][0] >= 'A' and words[1][0] <= 'Z':
    tmp = []
    if words[1][-1] != '.' and words[1][-1] != ',':
        tmp.append(words[1])
    else:
        tmp.append(words[1][:-1])
    tmp.append(2)
    myWords.append(tmp)
for i in range(2,len(words)):
    if words[i][0] >= 'A' and words[i][0] <= 'Z':
        if words[i-1][-1] != '.':
            tmp = []
            if words[i][-1] != '.' and words[i][-1] != ',':
                tmp.append(words[i])
            else:
                tmp.append(words[i][:-1])
            tmp.append(i+1)
            myWords.append(tmp)
if len(myWords) > 0:
    for i in range(0,len(myWords)):
        print('%i:%s' %(myWords[i][1], myWords[i][0]))
else:
    print('None')
