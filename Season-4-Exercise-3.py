import requests
from bs4 import BeautifulSoup
import mysql.connector
import os
#-----------------------------------------------------------------------------------------------
def clear():
    os.system('cls')
#-----------------------------------------------------------------------------------------------
def open_Connection():
    return mysql.connector.connect(user='root', 
                              password='12345',
                              host='127.0.0.1',
                              port=3307,
                              database='maktabkhooneh')
#-----------------------------------------------------------------------------------------------
def close_Connection(cnx):
    cnx.close()
#-----------------------------------------------------------------------------------------------
def checkTables(tablename):
    cnx = open_Connection()
    stmt = "SHOW TABLES LIKE '%s' "% ('%'+str(tablename)+'%')
    cursor = cnx.cursor()
    cursor.execute(stmt)
    result = cursor.fetchone()  
    if result == None:
        createTables(cnx, tablename)
#-----------------------------------------------------------------------------------------------
def createTables(cnx, tablename):
    stmt = "CREATE TABLE %s ( carName varchar(255), carType varchar(255), carMileage varchar(255), carPrice varchar(255)); " % (tablename)
    cursor = cnx.cursor()
    cursor.execute(stmt)        
    cnx.commit()
#-----------------------------------------------------------------------------------------------
def add_Info(tablename, name, type, mileage, price):
    cnx = open_Connection()
    cursor = cnx.cursor()
    add_car = """INSERT INTO %s (carName, carType, carMileage, carPrice) VALUES ('%s', '%s', '%s', '%s')""" %(tablename, name, type, mileage, price)
    cursor.execute(add_car)
    cnx.commit()
    close_Connection(cnx)
#-----------------------------------------------------------------------------------------------
def get_site_info(car):
    url_part_1 = 'https://www.truecar.com/used-cars-for-sale/listings/'
    url_part_2 = car
    url_part_3 = '/location-conneaut-lake-pa/'
    url_final = url_part_1 + url_part_2 + url_part_3
    try:
        print('Start Loading ...')
        req = requests.get(url_final)
        return True , req
    except Exception as err:
        print('Oooops! ' + str(err))
        return False , 0
#-----------------------------------------------------------------------------------------------
def parse_site_info(req):
    print('Start Processing ...')
    soup = BeautifulSoup(req.text,'html.parser')
    vals = soup.find_all('div' , attrs={'class' : 'card-content order-3 vehicle-card-body'})
    list_of_cars = []
    for val in vals:
        car = []
        val_info = str(val)
        soup = BeautifulSoup(val_info,'html.parser')
        val_name = soup.find('span' , attrs={'class' : 'truncate'})
        car.append(val_name.text)
        val_type = soup.find('div' , attrs={'class' : 'truncate text-xs'})
        car.append(val_type.text)
        val_Mileage = soup.find('div' , attrs={'class' : 'truncate text-xs' , 'data-test' : 'vehicleMileage'})
        car.append(val_Mileage.text)
        val_Price = soup.find('div' , attrs={'data-test' : 'vehicleCardPricingBlockPrice'})
        car.append(val_Price.text)
        list_of_cars.append(car)
    return list_of_cars
#----- Main ------------------------------------------------------------------------------------
clear()
tablename = 'Truecar'
checkTables(tablename)
carName = input('Please enter brand of car: (for example: BMW) :')
get_info , req = get_site_info(carName)
if get_info == True:
    if req.status_code == 200:
        cars = parse_site_info(req)
        if len(cars) > 0:
            for car in cars:
                add_Info(tablename, car[0], car[1], car[2], car[3])
            print('Insert %i cars to Database.' %(len(cars)))
print('End of Program.')
#-----------------------------------------------------------------------------------------------
