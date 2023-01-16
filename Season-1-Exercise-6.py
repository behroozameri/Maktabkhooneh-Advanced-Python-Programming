inputLen = int(input())
words = dict()
for i in range(0, inputLen):
    inputString = input()
    tmp = list(inputString.split(' '))
    tmp.reverse()
    value = tmp.pop()
    words[tmp.pop()] = value
    words[tmp.pop()] = value
    words[tmp.pop()] = value
inputString = input()
tmp = list(inputString.split(' '))
finalString = ''
for i in range(0, len(tmp)):
    finalString += words.get(tmp[i], tmp[i]) + ' '
print(finalString)
