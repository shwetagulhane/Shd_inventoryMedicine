import mysql.connector
import db_conf as con

#access to database connection
db=con.db
#prepare cursor object using cursor() method
cursor=db.cursor()

def InsertData(dbcolumn,htmlcolumn,tablename):
    print(dbcolumn,htmlcolumn)
    sql=''
    try:
        if tablename !='':
            if len(dbcolumn) == len(htmlcolumn):
                sql = "INSERT INTO "+tablename+"("
                for i in range(0,len(dbcolumn)):
                    if i == len(dbcolumn)-1:
                        sql = sql+dbcolumn[i]+") values"+"("
                    else:
                        sql = sql+dbcolumn[i]+","

                print(sql)

                for i in range(0,len(htmlcolumn)):
                    if i == len(htmlcolumn)-1:
                        sql = sql+"'"+htmlcolumn[i]+"'"+")"
                    else:
                        sql = sql+"'"+htmlcolumn[i]+"'"+","
                cursor.execute(sql)
                db.commit()
                return 1
            else:
                return "Columns Not Matching"
        else:
            return "Please Specify Table Name"
    except Exception as e:
        return str(e)
