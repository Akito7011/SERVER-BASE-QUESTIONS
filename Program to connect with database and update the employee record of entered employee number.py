import mysql.connector as mysql
sql=mysql.connect(host='localhost',user='root',password='Tanishq@2017')
if sql.is_connected():
    print('connected')
else:
    print('not connected')
cr=sql.cursor()
cr.execute('use office')
def modify():
    ID=int(input("Enter Employee ID to modify DATA"))
    print(":FIELD NAME: ID/NAME/GENDER/SALARY")
    mod=input("enter field name as shown above to modify: ")
    modify=input('enter updated data')
    cr.execute('update employ set {}="{}" where ID={}'.format(mod,modify,ID))
    sql.commit()
    print("record updated")
modify()
