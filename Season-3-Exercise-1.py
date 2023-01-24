import mysql.connector

def open_Connection():
    return mysql.connector.connect(user='root', 
                              password='12345',
                              host='127.0.0.1',
                              port=3307,
                              database='learn')

def close_Connection(cnx):
    cnx.close()

def add_employees():
    cnx = open_Connection()
    cursor = cnx.cursor()
    add_employee = """INSERT INTO employee (Name, Weight, Height) VALUES (%s, %s, %s)"""
    data_employee = ('Amin', 75, 180)
    cursor.execute(add_employee, data_employee)
    data_employee = ('Mahdi', 90, 190)
    cursor.execute(add_employee, data_employee)
    data_employee = ('Mohammad', 75, 175)
    cursor.execute(add_employee, data_employee)
    data_employee = ('Ahmad', 60, 175)
    cursor.execute(add_employee, data_employee)
    cnx.commit()
    close_Connection(cnx)

def get_employees_from_db():
    cnx = open_Connection()
    cursor = cnx.cursor()
    query = """SELECT * FROM employee"""
    cursor.execute(query)
    employeeList = []
    for (Name, Weight, Height) in cursor:
        tmp = []
        tmp.append(Name)
        tmp.append(Weight)
        tmp.append(Height)
        employeeList.append(tmp)
    cursor.close()
    close_Connection(cnx)
    return employeeList

def sort_employees(employeeList):
    employeeList.sort(key=lambda x: x[2], reverse=True)
    for i in range(0, len(employeeList)):
        for j in range(0, len(employeeList)):
            if employeeList[i][2] == employeeList[j][2]:
                if employeeList[i][1] < employeeList[j][1]:
                    employeeList[i],employeeList[j] = employeeList[j],employeeList[i]
    return employeeList

def print_employee_list(employeeList):
    for employee in employeeList:
        print(employee[0], employee[2], employee[1],)


#add_employees()
employeeList = get_employees_from_db()
employeeList = sort_employees(employeeList)
print_employee_list(employeeList)

