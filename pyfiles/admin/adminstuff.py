from flask import request,url_for,json,jsonify
from mysql.connector import Error
from werkzeug import secure_filename
import os,sys
import db_conf as con
import insertdata as ins
import updatedata as up
import datetime

#DB object for hospital databse
db = con.db
cursor=db.cursor()

def getAllDistrict():
    try:
        sql="select * from admin_district where deletestatus='{0}'"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)

def getAllWard():
    try:
        sql="select * from admin_wardname where deletestatus='{0}'"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)
