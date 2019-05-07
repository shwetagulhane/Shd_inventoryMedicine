import mysql.connector
import datetime as dt
import time as tm
import os,sys
import db_conf as con

db = con.db
cursor=db.cursor()

now = dt.datetime.now()
dtd = now.strftime('%Y')


def getNewRegno():
    sql="SELECT regno FROM patient_registration ORDER BY pid DESC LIMIT 1"
    cursor.execute(sql)
    value = cursor.fetchone()

    if not value:
        value=str(1)
    else:
        if int(value[0][:4])<int(dtd):
            value=str(1)
        else:
            value = int(value[0][7:])+1
    return dtd+"SHD"+str(value)
