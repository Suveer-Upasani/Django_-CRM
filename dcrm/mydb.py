#Install MSQL
#pip install mysql
#pip install mysqlconnector-python  

import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='T1ger@2025'
)

#prepare a cursor object
cursorObject=dataBase.cursor()
#create a database
cursorObject.execute("CREATE DATABASE Suveer")

print("All Done!")