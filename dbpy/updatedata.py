import mysql.connector
import db_conf as con

#access to database connection
db=con.db
#prepare cursor object using cursor() method
cursor=db.cursor()

def UpdateData(dbcolumn,htmlcolumn,tablename):
    sql=''
    try:
        if tablename !='':
            if len(dbcolumn) == len(htmlcolumn):
                sql = "UPDATE "+tablename+" SET "
                for i in range(0,len(dbcolumn)):
                    if i == len(dbcolumn)-1:
                        sql = sql+" WHERE "+dbcolumn[i]+"= '"+htmlcolumn[i]+"'"
                    else:
                        if i == len(dbcolumn)-2:
                            sql = sql+dbcolumn[i]+"= '"+htmlcolumn[i]+"'"
                        else:
                            sql = sql+dbcolumn[i]+"= '"+htmlcolumn[i]+"',"
                print(sql)
                cursor.execute(sql)
                db.commit()
                return 1
            else:
                return "Columns Not Matching"
        else:
            return "Please Specify Table Name"
    except Exception as e:
        return str(e)
