import mysql.connector
import re 

def check_email(email):
    regex = '^[A-Za-z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]\w{2,3}$'   
    return True if re.search(regex,email) else False

def check_password(password):
    regex = '^[A-Za-z0-9]*$'    
    return True if re.search(regex,password) else False

def open_Connection():
    return mysql.connector.connect(user='root', 
                              password='12345',
                              host='127.0.0.1',
                              port=3307,
                              database='learn')

def close_Connection(cnx):
    cnx.close()

def add_user(username, password):
    cnx = open_Connection()
    cursor = cnx.cursor()
    add_user = """INSERT INTO userinfo (username, password) VALUES (%s, %s)"""
    data_user = (username, password)
    cursor.execute(add_user, data_user)
    cnx.commit()
    close_Connection(cnx)

def get_userinfo():
    while True:
        emailString = input("Please Enter your Email: ")
        passwordString = input("Please Enter your Password: ")
        if check_email(emailString) and check_password(passwordString):
            return emailString, passwordString
        print('Email or Password in not Valid.')


username,password = get_userinfo()
add_user(username,password)


