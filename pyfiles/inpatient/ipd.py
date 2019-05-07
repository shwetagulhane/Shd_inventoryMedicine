from flask import request,url_for,json,jsonify
from mysql.connector import Error
import os,sys
import db_conf as con
newpath = os.getcwd()+"/dbpy"
sys.path.insert(0, newpath)
import insertdata as ins
import updatedata as up
db = con.db
cursor=db.cursor()

def getAdmitPatientData(ipdid):
    try:
        sql = "select i.*,TIME_FORMAT(i.ipdtime,'%H:%i'),w.wid,w.wname from ipdvisit i,admin_wardname w where i.wardid=w.wid AND ipdid='{}'".format(ipdid)
        cursor.execute(sql)
        return(cursor.fetchall())
    except Exception as e:
        return str(e)


def getAllAdmitPatientData(regno):
    try:
        sql = "select i.*,w.wid,w.wname from ipdvisit i,admin_wardname w where i.wardid=w.wid AND regno='{}' order by ipddate DESC".format(regno)
        cursor.execute(sql)
        return(cursor.fetchall())
    except Exception as e:
        return str(e)

def getLatestAdmitPatientData(regno):
    try:
        sql = "select p.*,o.complaint,o.ptype from patient_registration p, opdvisit o where p.regno = o.regno AND  o.regno= '{}' order by o.vdate DESC limit 1".format(regno)
        cursor.execute(sql)
        return(cursor.fetchall())
    except Exception as e:
        return str(e)

# THIS FUNCTION WILL INSERT A NEW ROW IN IPDVISIT TABLE.

def visitIpd():
    gscheme=request.form['gscheme']
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "ipdvisit"
    try:
        if request.method == 'POST':
            dbcolumn.append('regno')
            dbcolumn.append('complaint')
            dbcolumn.append('patientfrom')
            dbcolumn.append('ipddate')
            dbcolumn.append('ipdtime')
            dbcolumn.append('ptype')
            dbcolumn.append('govscheme')
            dbcolumn.append('urnno')
            dbcolumn.append('advmoney')
            dbcolumn.append('moneyreceivedby')
            dbcolumn.append('wardid')


            htmlcolumn.append(request.form['regno'])
            htmlcolumn.append(request.form['complaint'])
            htmlcolumn.append(request.form['patientfrom'])
            htmlcolumn.append(request.form['ipddate'])
            htmlcolumn.append(request.form['ipdtime'])
            htmlcolumn.append(request.form['ptype'])

            if gscheme == 'eligible':
                htmlcolumn.append(request.form['govscheme'])
            else:
                htmlcolumn.append(request.form['gscheme'])

            htmlcolumn.append(request.form['urnno'])
            htmlcolumn.append(request.form['advmoney'])
            htmlcolumn.append(request.form['moneyreceivedby'])
            htmlcolumn.append(request.form['wardid'])

            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

# THIS FUNCTION WILL UPDATE THE OLD INFORMATION IN IPDVISIT TABLE.

def visitIpdUpdate():
    gscheme=request.form['gscheme']
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "ipdvisit"
    try:
        if request.method == 'POST':
            dbcolumn.append('complaint')
            dbcolumn.append('patientfrom')
            dbcolumn.append('ipddate')
            dbcolumn.append('ipdtime')
            dbcolumn.append('govscheme')
            dbcolumn.append('urnno')
            dbcolumn.append('advmoney')
            dbcolumn.append('moneyreceivedby')
            dbcolumn.append('wardid')
            dbcolumn.append('ipdid')# The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF dbcolumn"


            htmlcolumn.append(request.form['complaint'])
            htmlcolumn.append(request.form['patientfrom'])
            htmlcolumn.append(request.form['ipddate'])
            htmlcolumn.append(request.form['ipdtime'])

            if gscheme == 'eligible':
                htmlcolumn.append(request.form['govscheme'])
            else:
                htmlcolumn.append(request.form['gscheme'])

            htmlcolumn.append(request.form['urnno'])
            htmlcolumn.append(request.form['advmoney'])
            htmlcolumn.append(request.form['moneyreceivedby'])
            htmlcolumn.append(request.form['wardid'])
            htmlcolumn.append(request.form['ipdid'])# The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF htmlcolumn"

            # Here we are calling UpdateData that have a  common  code for update record.
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)
