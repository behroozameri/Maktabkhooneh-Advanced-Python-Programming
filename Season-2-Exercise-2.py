from datetime import date

def age(birthdate):
    today = date. today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

inputString = input().split('/')
inputString = list(map(lambda x:int(x), inputString))
if inputString[1] > 12 or inputString[1] < 1:
    print('WRONG')
elif inputString[2] > 31 or inputString[2] < 1:
    print('WRONG')
else:
    print(age(date(inputString[0], inputString[1], inputString[2])))
