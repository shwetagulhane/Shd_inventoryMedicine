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




def getAllPatientVisitData(opdid):
    try:
        if request.method == 'POST':
            sql="select *,TIME_FORMAT(vtime,'%H:%i') from opdvisit where opdid='{}'".format(opdid)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        return str(e)

def getOldPatientRegno():
    try:
        if request.method == 'POST':
            regno = request.form['regno']
            sql="select * from patient_registration where regno='{}'".format(regno)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        return str(e)
def getOldPatientFName():
    try:
        if request.method == 'POST':
            name = request.form['pfname']
            sql="select * from patient_registration where pfname LIKE '%{}%'".format(name)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        return str(e)
def getOldPatientContact():
    try:
        if request.method == 'POST':
            contact = request.form['contactno']
            sql="select * from patient_registration where contactno='{}'".format(contact)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        return str(e)

def getOldPatientAadhar():
    try:
        if request.method == 'POST':
            aadhar = request.form['aadharNo']
            sql="select * from patient_registration where aadharNo='{}'".format(aadhar)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        return str(e)

def getOldPatientAddress():
    try:
        if request.method == 'POST':
            address = request.form['address']
            sql="select * from patient_registration where address LIKE '%{}%'".format(address)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        return str(e)

def getPatientVisitData(regno):
        try:
            if request.method == 'POST':
                sql="select v.opdid,v.complaint,v.vdate,v.height,v.weight,v.bmi,v.systolic,v.diastolic,v.pulse,v.temp,v.rrate  from patient_registration p,opdvisit v where p.regno=v.regno AND v.regno='{}'".format(regno)
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except Exception as e:
            return str(e)

#--------------THIS FUNCTION WILL RETURN TODAY PATIENT VISIT DATA------------
def getTodayPatientVisitData(regno,todaydate):
        try:
            if request.method == 'POST':
                sql="select * from opdvisit  where regno='{}' AND vdate='{}'".format(regno,todaydate)
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except Exception as e:
            return str(e)

#-------------THIS FUNCTION WILL RETURN LIST OF DIAGNOSIS ACCORDING TO FILTER VARIABLE-----------------------------
def getDiagnosis():
        dia = request.form['pdiagno']
        record=[]
        print("i am here")
        try:
            if request.method == 'POST':
                sql="select diagnosis,did from admin_diagno  where diagnosis LIKE '%{}%'".format(dia)
                cursor.execute(sql)
                result = cursor.fetchall()
                if cursor.rowcount >0:
                    for i in range(0,len(result)):
                        record.append(str(result[i][1])+"# "+result[i][0])
                    return record
                else:
                    return 0
        except Exception as e:
            return str(e)

def getOpdConsultHistory(regno):
    try:
        if request.method == 'POST':
            sql="select * from opdClinicalHistory  where regno='{}'".format(regno)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        return str(e)

def getOpdConsultRefer(regno):
    try:
        if request.method == 'POST':
            sql="select * from opdreferInfo  where regno='{}'".format(regno)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        return str(e)

def getOpdConsultDiagnosis(regno):
    try:
        if request.method == 'POST':
            sql="select * from opdDiagnosis  where regno='{}'".format(regno)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        return str(e)

def visitOpdInsert():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "opdvisit"
    try:
        if request.method == 'POST':
#Name of database Attribute
            dbcolumn.append('regno')
            dbcolumn.append('ptype')
            dbcolumn.append('vdate')
            dbcolumn.append('vtime')
            dbcolumn.append('height')
            dbcolumn.append('weight')
            dbcolumn.append('bmi')
            dbcolumn.append('temp')
            dbcolumn.append('pulse')
            dbcolumn.append('rrate')
            dbcolumn.append('systolic')
            dbcolumn.append('diastolic')
            dbcolumn.append('complaint')

#Name of html component e.g request.form['nameofcomponenet']
            htmlcolumn.append(request.form['regno'])
            htmlcolumn.append(request.form['ptype'])
            htmlcolumn.append(request.form['vdate'])
            htmlcolumn.append(request.form['vtime'])
            htmlcolumn.append(request.form['height'])
            htmlcolumn.append(request.form['weight'])
            htmlcolumn.append(request.form['bmi'])
            htmlcolumn.append(request.form['temp'])
            htmlcolumn.append(request.form['pulse'])
            htmlcolumn.append(request.form['rrate'])
            htmlcolumn.append(request.form['systolic'])
            htmlcolumn.append(request.form['diastolic'])
            htmlcolumn.append(request.form['complaint'])

            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


def insertOpdConsultRefer():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "opdreferInfo"
    try:
        if request.method == 'POST':
            #Name of database Attribute
            dbcolumn.append('opdid')
            dbcolumn.append('regno')
            dbcolumn.append('reason')
            dbcolumn.append('refdate')
            dbcolumn.append('hname')
            dbcolumn.append('referby')
            dbcolumn.append('referto')


            #Name of html component e.g request.form['nameofcomponenet']
            htmlcolumn.append(request.form['opdid'])
            htmlcolumn.append(request.form['regno'])
            htmlcolumn.append(request.form['reason'])
            htmlcolumn.append(request.form['refdate'])
            htmlcolumn.append(request.form['hname'])
            htmlcolumn.append(request.form['referby'])
            htmlcolumn.append(request.form['referto'])

            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


def insertOpdConsultHistory():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "opdClinicalHistory"
    try:
        if request.method == 'POST':
            #Name of database Attribute
            dbcolumn.append('opdid')
            dbcolumn.append('regno')
            dbcolumn.append('hiscli')
            dbcolumn.append('hcdate')
            dbcolumn.append('docid')


            #Name of html component e.g request.form['nameofcomponenet']
            htmlcolumn.append(request.form['opdid'])
            htmlcolumn.append(request.form['regno'])
            htmlcolumn.append(request.form['hiscli'])
            htmlcolumn.append(request.form['hcdate'])
            htmlcolumn.append(request.form['docid'])


            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

def insertOpdDiagnosis():
    result=''
    tablename = "opdDiagnosis"
    rowno=len(request.form.getlist('diagnosisId'))
    diaId = request.form.getlist('diagnosisId') #Has Multiple Value
    diaType = request.form.getlist('diagnosisType')  #Has Multiple Value
    try:
        if request.method == 'POST':



            for i in range(rowno):
                dbcolumn = []
                htmlcolumn = []
                #Name of database Attribute
                dbcolumn.append('opdid')
                dbcolumn.append('regno')
                dbcolumn.append('diagnosisId')
                dbcolumn.append('diagnosisType')
                dbcolumn.append('diagnosisDate')

                #Name of html component e.g request.form['nameofcomponenet']
                htmlcolumn.append(request.form['opdid'])
                htmlcolumn.append(request.form['regno'])
                htmlcolumn.append(diaId[i])
                htmlcolumn.append(diaType[i])
                htmlcolumn.append(request.form['diagnosisDate'])

                # Here we are calling InsertData that have a  common  code for insert record.
                result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


def insertOpdDocUpload(uploadloc):
    result=''
    tablename = "opdDocument"
    rowno=len(request.form.getlist('doc_name'))
    print(rowno)
    regno = request.form['regno']
    docname = request.form.getlist('doc_name') #Has Multiple Value
    docdate = request.form.getlist('doc_date') #Has Multiple Value
    docloc = request.files.getlist('doc_file') #Has Multiple Value

    docfrom = request.form.getlist('doc_from') #Has Multiple Value
    entrydate=request.form['entrydate']
    print(docname,docdate)
    try:
        if request.method == 'POST':
            for i in range(rowno):
                dbcolumn = []
                htmlcolumn = []
                #Name of database Attribute
                dbcolumn.append('regno')
                dbcolumn.append('doc_name')
                dbcolumn.append('doc_date')
                dbcolumn.append('doc_file_loc')
                dbcolumn.append('doc_from')
                dbcolumn.append('entry_date')

                #Name of html component e.g request.form['nameofcomponenet']
                htmlcolumn.append(regno)
                htmlcolumn.append(docname[i])
                htmlcolumn.append(docdate[i])

                fname,fileext = os.path.splitext(docloc[i].filename)
                filename=secure_filename(regno+'_'+'{0:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now())+'_'+fname+fileext)
                dst_path=os.path.join(uploadloc, filename)
                docloc[i].save(dst_path)

                htmlcolumn.append(filename)
                htmlcolumn.append(docfrom[i])
                htmlcolumn.append(entrydate)
                #print(request.form['opdid'],diaId[i],diaType[i],request.form['diagnosisDate'])
                # Here we are calling InsertData that have a  common  code for insert record.
                result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

#UPDATE PATIENT VISIT DATA
def opdVisitUpdate():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "opdvisit"
    try:
        if request.method == 'POST':
            #Name of database Attribute
            dbcolumn.append('vdate')
            dbcolumn.append('vtime')
            dbcolumn.append('height')
            dbcolumn.append('weight')
            dbcolumn.append('bmi')
            dbcolumn.append('temp')
            dbcolumn.append('pulse')
            dbcolumn.append('rrate')
            dbcolumn.append('systolic')
            dbcolumn.append('diastolic')
            dbcolumn.append('complaint')
            dbcolumn.append('opdid')# The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF dbcolumn"

            #Name of html component e.g request.form['nameofcomponenet']

            htmlcolumn.append(request.form['vdate'])
            htmlcolumn.append(request.form['vtime'])
            htmlcolumn.append(request.form['height'])
            htmlcolumn.append(request.form['weight'])
            htmlcolumn.append(request.form['bmi'])
            htmlcolumn.append(request.form['temp'])
            htmlcolumn.append(request.form['pulse'])
            htmlcolumn.append(request.form['rrate'])
            htmlcolumn.append(request.form['systolic'])
            htmlcolumn.append(request.form['diastolic'])
            htmlcolumn.append(request.form['complaint'])
            htmlcolumn.append(request.form['opdid'])  # The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF htmlcolumn"

            # Here we are calling UpdateData that have a  common  code for update record.
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)
