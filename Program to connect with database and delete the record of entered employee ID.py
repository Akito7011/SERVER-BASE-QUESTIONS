import pymysql.connector as mysql
sql=mysql.connect(host='localhost',user='root',password='Tanishq@2017')
if sql.is_connected():
    print('connected')
else:
    print('not connected')
cr=sql.cursor()
cr.execute('use office')
def delete():
    ID=int(input("Enter Employee ID to delete DATA: "))
    cr.execute('delete from employ where ID={}'.format(ID))
    sql.commit()
    print("record deleted")
delete()
