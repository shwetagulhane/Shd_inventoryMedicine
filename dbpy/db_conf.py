import mysql.connector

#open database connection
db = mysql.connector.connect(host="localhost",user="root",password="123",database="shd_hospital")
dbadmin=mysql.connector.connect(host="localhost",user="root",password="123",database="SHDadmin")
