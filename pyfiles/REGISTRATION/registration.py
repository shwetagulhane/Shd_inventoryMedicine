from flask import request,url_for,json,jsonify
from mysql.connector import Error
import os,sys

import db_conf as con
import datetime as dt,time as tm

db = con.db
cursor=db.cursor()

now = dt.datetime.now()
dtd = now.strftime('%Y')

import insertdata as ins
import updatedata as up

#This function will return entire row of patient_registration with respect to RegNo.
def getPatient_Registration_All(regno):
    try:
        sql="select p.*,TIME_FORMAT(p.regtime,'%H:%i'),d.did,d.disname from patient_registration p,admin_district d where p.district=d.did AND regno='{}'".format(regno)
        cursor.execute(sql)
        return cursor.fetchall()

    except Exception as e:
        return str(e)

#This function will insert a new record in table "patient_registration" for new patient.
def newRegistration():
    regno = request.form['regno']
    pclass= request.form['pclass']
    dbcolumn = []
    htmlcolumn = []
    tablename = "patient_registration"
    result=''
    try:
        if request.method == 'POST':
            dbcolumn.append('regno')
            dbcolumn.append('pfname')
            dbcolumn.append('pmname')
            dbcolumn.append('psname')
            dbcolumn.append('rtype')
            dbcolumn.append('rfname')
            dbcolumn.append('rmname')
            dbcolumn.append('rsname')
            dbcolumn.append('regdate')
            dbcolumn.append('regtime')
            dbcolumn.append('age')
            dbcolumn.append('agetype')
            dbcolumn.append('sex')
            dbcolumn.append('education')
            dbcolumn.append('occupation')
            dbcolumn.append('contactno')
            dbcolumn.append('pclass')
            dbcolumn.append('village')
            dbcolumn.append('tahsil')
            dbcolumn.append('district')
            dbcolumn.append('address')
            dbcolumn.append('cast')
            dbcolumn.append('aadharNo')
            dbcolumn.append('rationcard')

            htmlcolumn.append(regno)
            htmlcolumn.append(request.form['pfname'])
            htmlcolumn.append(request.form['pmname'])
            htmlcolumn.append(request.form['psname'])
            htmlcolumn.append(request.form['rtype'])
            htmlcolumn.append(request.form['rfname'])
            htmlcolumn.append(request.form['rmname'])
            htmlcolumn.append(request.form['rsname'])
            htmlcolumn.append(request.form['regdate'])
            htmlcolumn.append(request.form['regtime'])
            htmlcolumn.append(request.form['age'])
            htmlcolumn.append(request.form['agetype'])
            htmlcolumn.append(request.form['sex'])
            htmlcolumn.append(request.form['education'])
            htmlcolumn.append(request.form['occupation'])
            htmlcolumn.append(request.form['contactno'])

            if pclass == 'Company':
                htmlcolumn.append(request.form['cname'])
            else:
                htmlcolumn.append(request.form['pclass'])

            htmlcolumn.append(request.form['village'])
            htmlcolumn.append(request.form['tahsil'])
            htmlcolumn.append(request.form['district'])
            htmlcolumn.append(request.form['address'])
            htmlcolumn.append(request.form['cast'])
            htmlcolumn.append(request.form['aadharNo'])
            htmlcolumn.append(request.form['rationcard'])

            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


#This function will UPDATE the OLD record in the basis of REGNO in table "patient_registration".
def updateRegistration():
    regno = request.form['regno']
    pclass= request.form['pclass']
    dbcolumn = []
    htmlcolumn = []
    tablename = "patient_registration"
    result=''
    try:
        if request.method == 'POST':
            dbcolumn.append('pfname')
            dbcolumn.append('pmname')
            dbcolumn.append('psname')
            dbcolumn.append('rtype')
            dbcolumn.append('rfname')
            dbcolumn.append('rmname')
            dbcolumn.append('rsname')
            dbcolumn.append('regdate')
            dbcolumn.append('regtime')
            dbcolumn.append('age')
            dbcolumn.append('agetype')
            dbcolumn.append('sex')
            dbcolumn.append('education')
            dbcolumn.append('occupation')
            dbcolumn.append('contactno')
            dbcolumn.append('pclass')
            dbcolumn.append('village')
            dbcolumn.append('tahsil')
            dbcolumn.append('district')
            dbcolumn.append('address')
            dbcolumn.append('cast')
            dbcolumn.append('aadharNo')
            dbcolumn.append('rationcard')
            dbcolumn.append('regno') # The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF dbcolumn"


            htmlcolumn.append(request.form['pfname'])
            htmlcolumn.append(request.form['pmname'])
            htmlcolumn.append(request.form['psname'])
            htmlcolumn.append(request.form['rtype'])
            htmlcolumn.append(request.form['rfname'])
            htmlcolumn.append(request.form['rmname'])
            htmlcolumn.append(request.form['rsname'])
            htmlcolumn.append(request.form['regdate'])
            htmlcolumn.append(request.form['regtime'])
            htmlcolumn.append(request.form['age'])
            htmlcolumn.append(request.form['agetype'])
            htmlcolumn.append(request.form['sex'])
            htmlcolumn.append(request.form['education'])
            htmlcolumn.append(request.form['occupation'])
            htmlcolumn.append(request.form['contactno'])

            if pclass == 'Company':
                htmlcolumn.append(request.form['cname'])
            else:
                htmlcolumn.append(request.form['pclass'])

            htmlcolumn.append(request.form['village'])
            htmlcolumn.append(request.form['tahsil'])
            htmlcolumn.append(request.form['district'])
            htmlcolumn.append(request.form['address'])
            htmlcolumn.append(request.form['cast'])
            htmlcolumn.append(request.form['aadharNo'])
            htmlcolumn.append(request.form['rationcard'])
            htmlcolumn.append(regno) # The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF htmlcolumn"

            # Here we are calling UpdateData that have a  common  code for update record.
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


#This method will return new Registration Number.
def getNewRegno():
    try:
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
    except Exception as e:
        return str(e)
