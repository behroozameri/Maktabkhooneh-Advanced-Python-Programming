import re 

def check_email(email):
    regex = '^[A-Za-z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]\w+$'   
    return True if re.search(regex,email) else False


inputString = input()
if check_email(inputString):
    print('OK')
else:
    print('WRONG')
