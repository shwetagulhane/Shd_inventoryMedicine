from flask import request,url_for,json,jsonify
from mysql.connector import Error
import os,sys
import datetime
import db_conf as con
import datetime as dt,time as tm
import insertdata as ins
import updatedata as up

db = con.db
cursor=db.cursor()


##---here we are inserting new medicine
def AddNewMedicne():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "main_medicine"
    try:
        if request.method == 'POST':
            #Name of database Attribute

            dbcolumn.append('drugname')
            dbcolumn.append('medicine_type')
            dbcolumn.append('min_value')
            dbcolumn.append('max_value')


            #Name of html component e.g request.form['nameofcomponenet']
            htmlcolumn.append(request.form['drug_name'])
            htmlcolumn.append(request.form['med_type'])
            htmlcolumn.append(request.form['min_value'])
            htmlcolumn.append(request.form['max_value'])



            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


##------Inserting inventory details-----

def New_Inventory():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "inventory_detail"
    row=len(request.form.getlist('batch_no'))
    
    drug = request.form.getlist('drug_id') #Has Multiple Value
    print(drug);
    hsn = request.form.getlist('hsn_code') #Has Multiple Value
    print(hsn);
    qty = request.form.getlist('quantity') #Has Multiple Value
    print(qty);
    Rate = request.form.getlist('rate') #Has Multiple Value
    print(Rate);
    drug_name = request.form.getlist('drugname') #Has Multiple Value
    print(drug_name);
    batch_no = request.form.getlist('batch_no') #Has Multiple Value
    print(batch_no);
    expiry = request.form.getlist('expiry_date') #Has Multiple Value
    print(expiry);
    mfg_d = request.form.getlist('manufacturing_date') #Has Multiple Value
    print(mfg_d);
    qtymg = request.form.getlist('quantity_mg') #Has Multiple Value
    print(qtymg);
    dis = request.form.getlist('discount') #Has Multiple Value
    print(dis);
    free = request.form.getlist('free_med') #Has Multiple Value
    print(free);
    Mrp = request.form.getlist('mrp') #Has Multiple Value
    print(Mrp);
    pak = request.form.getlist('pack') #Has Multiple Value
    print(pak);
    tax = request.form.getlist('taxable_amount') #Has Multiple Value
    print(tax);
    cgt= request.form.getlist('cgst') #Has Multiple Value
    print(cgt);
    sgt = request.form.getlist('sgst') #Has Multiple Value
    print(sgt);
    amount = request.form.getlist('amt') #Has Multiple Value
    print(amount);
    rack = request.form.getlist('rack_no') #Has Multiple Value
    print(rack);
    tempqty = request.form.getlist('temp_quantity') #Has Multiple Value
    print(tempqty);
    ''' try:
        if request.method == 'POST':

            for i in range(row):
		
			dbcolumn.append('distdet_id')
			dbcolumn.append('med_id')
			dbcolumn.append('date')
			dbcolumn.append('hsn_code')
			dbcolumn.append('quantity')
			dbcolumn.append('rate')
			
			dbcolumn.append('batch_no')
			dbcolumn.append('expiry_date')
			dbcolumn.append('manufacturing_date')
			dbcolumn.append('quantity_mg')
			dbcolumn.append('discount')
			dbcolumn.append('free_med')
			dbcolumn.append('mrp')
			dbcolumn.append('pack')
			dbcolumn.append('taxable_amt')
			dbcolumn.append('cgst')
			dbcolumn.append('sgst')
			dbcolumn.append('amount')
			dbcolumn.append('rack_no')
			dbcolumn.append('temp_quantity')
			#Name of html component e.g request.form['nameofcomponenet']
			htmlcolumn.append(request.form['dist_type_id'])
			htmlcolumn.append(request.form['date'])
			print('date');
			htmlcolumn.append(drug[i])
			print(drug[i]);
			htmlcolumn.append(hsn[i])
			htmlcolumn.append(qty[i])
			htmlcolumn.append(Rate[i])
			
			htmlcolumn.append(batch_no[i])
			htmlcolumn.append(expiry[i])
			htmlcolumn.append(mfg_d[i])
			htmlcolumn.append(qtymg[i])
			htmlcolumn.append(dis[i])
			htmlcolumn.append(free[i])
			htmlcolumn.append(Mrp[i])
			htmlcolumn.append(pak[i])
			htmlcolumn.append(tax[i])
			htmlcolumn.append(cgt[i])
			htmlcolumn.append(sgt[i])
			htmlcolumn.append(amount[i])
			htmlcolumn.append(rack[i])
			htmlcolumn.append(tempqty[i])
			result = ins.InsertData(dbcolumn,htmlcolumn,tablename)'''
			#return 1
    #except Exception as e:
			#return str(e)

##----here we are fetching data from distributor detail and distributor detail type for inventory table--
#def GetId():
	#try:
		#sql="select "
		#cursor.execute(sql)
		#return cursor.fetchall()
	#except Exception as e:
		#return str(e)
	




##---Here we are inserting new distributor details----
def AddNewDistributor():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "distributor_detail"
    try:
        if request.method == 'POST':
            ##Name of database Attribute


            dbcolumn.append('distributor_name')
            dbcolumn.append('dist_type_id')
            dbcolumn.append('address')
            dbcolumn.append('emailid')
            dbcolumn.append('contact_no')
            dbcolumn.append('invoice_no')
            dbcolumn.append('drug_license')
            dbcolumn.append('gst_no')
            dbcolumn.append('aadhar_no')
            dbcolumn.append('pancard_no')



            ##Name of html component e.g request.form['nameofcomponenet']
            htmlcolumn.append(request.form['distributor_name'])
            htmlcolumn.append(request.form['dist_type_id'])
            htmlcolumn.append(request.form['address'])
            htmlcolumn.append(request.form['emailid'])
            htmlcolumn.append(request.form['contact_no'])
            htmlcolumn.append(request.form['invoice_no'])
            htmlcolumn.append(request.form['drug_license'])
            htmlcolumn.append(request.form['gst_no'])
            htmlcolumn.append(request.form['aadhar_no'])
            htmlcolumn.append(request.form['pancard_no'])


            ## Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


def Outward_detail():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "outward_detail"
    try:
        if request.method == 'POST':
            #Name of database Attribute
            dbcolumn.append('issued_date')
            dbcolumn.append('person_name')
            dbcolumn.append('time')


            #Name of html component e.g request.form['nameofcomponenet']
            htmlcolumn.append(request.form['issued_date'])
            htmlcolumn.append(request.form['person_name'])
            htmlcolumn.append(request.form['time'])

            # Here we are calling InsertData that have a  common  code for insert record.
            result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)

##---here we are fetching all distributor type
def GetAllDistributorType():
	try:
		sql="Select * from distributor_type_detail"
		cursor.execute(sql)
		return cursor.fetchall()
	except Exception as e:
		return str(e)

##---here we are fetching all distributor name
def GetAll_DistributorName(dist_type_id):
	try:
		sql="select distdet_id,distributor_name from distributor_detail where dist_type_id='{}'".format(dist_type_id)
		cursor.execute(sql)
		return cursor.fetchall()
	except Exception as e:
		return str(e)

def getDistributorAllData(distributor_id):
	try:
		sql="select dn.*,dt.dist_type_name from distributor_detail dn,distributor_type_detail dt where dn.dist_type_id = dt.dist_type_id AND deletestatus='0' AND dn.distdet_id='{}'".format(distributor_id)
		cursor.execute(sql)
		return cursor.fetchall()
	except Exception as e:
		return str(e)

#----here we are getting all drugname--
def getDrugname():
    hint = str(request.form['drugname'])
    arr_rows=[]

    if len(hint)>=3:
        
        sql = "select drugname,UPPER(medicine_type) from main_medicine where drugname LIKE'{}%'".format(hint)
        cursor.execute(sql)
        dt = cursor.fetchall()
        for i in range(0,len(dt)):
            med = dt[i][0] + " > [" + dt[i][1] + "]"
            arr_rows.append(med)
        return arr_rows
    else:
        return arr_rows
        
        
#----here we are separating drug name and drug type

def getDrugTypeName(drugtype):
	arr_data=[]
	drugname,drugtype=drugtype.split('>')
	drugtype = drugtype[2:-1]
	try:
		sql = "select med_id,drugname,UPPER(medicine_type) from main_medicine where drugname='{}' AND medicine_type='{}' ".format(drugname,drugtype)
		cursor.execute(sql)
		drugdata =cursor.fetchall()
		arr_data.append(str(drugdata[0][0]))
		arr_data.append(drugdata[0][1])
		arr_data.append(drugdata[0][2])
		
		return arr_data
		
	except Exception as e:
		return str(e)

	


#----here we update distributor details
def UpdateDistributor():
    dbcolumn = []
    htmlcolumn = []
    result=''
    tablename = "distributor_detail"
    try:
        if request.method == 'POST':
            ##Name of database Attribute


            dbcolumn.append('distributor_name')
            dbcolumn.append('dist_type_id')
            dbcolumn.append('address')
            dbcolumn.append('emailid')
            dbcolumn.append('contact_no')
            dbcolumn.append('invoice_no')
            dbcolumn.append('drug_license')
            dbcolumn.append('gst_no')
            dbcolumn.append('aadhar_no')
            dbcolumn.append('pancard_no')
            dbcolumn.append('distdet_id')# The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF dbcolumn"


            ##Name of html component e.g request.form['nameofcomponenet']
            htmlcolumn.append(request.form['distributor_name'])
            htmlcolumn.append(request.form['dis_type_name'])
            htmlcolumn.append(request.form['address'])
            htmlcolumn.append(request.form['emailid'])
            htmlcolumn.append(request.form['contact_no'])
            htmlcolumn.append(request.form['invoice_no'])
            htmlcolumn.append(request.form['drug_license'])
            htmlcolumn.append(request.form['gst_no'])
            htmlcolumn.append(request.form['aadhar_no'])
            htmlcolumn.append(request.form['pancard_no'])
            htmlcolumn.append(request.form['distributor_id'])# The column name on the basis of we update record "MUST BE THE LAST ELEMENT OF htmlcolumn"



            # Here we are calling UpdateData that have a  common  code for insert record.
            result = up.UpdateData(dbcolumn,htmlcolumn,tablename)
            return result
    except Exception as e:
        return str(e)


#-----adding new distributor type(admin panel)
def AddDistributorType():
	dbcolumn = []
	htmlcolumn = []
	result=''
	tablename = "distributor_type_detail"
	try:
		if request.method == 'POST':
			##Name of database Attribute
			dbcolumn.append('dist_type_name')

			##Name of html component e.g request.form['nameofcomponenet']
			htmlcolumn.append(request.form['dist_type_name'])
			result = ins.InsertData(dbcolumn,htmlcolumn,tablename)
			return result
	except Exception as e:
		return str(e)

