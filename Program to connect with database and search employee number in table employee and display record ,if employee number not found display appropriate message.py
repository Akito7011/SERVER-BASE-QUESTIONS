import mysql.connector as mysql
sql=mysql.connect(host='localhost',user='root',password='Tanishq@2017')
if sql.is_connected():
    print('connected')
else:
    print('not connected')
cr=sql.cursor()
cr.execute('use office')
def display():
    ans='y'
    while ans=='y':
        ID=int(input("enter emp ID to search for record: "))
        cr.execute('select* from employ where ID={}'.format(ID))
        r=cr.fetchall()
        if cr.rowcount>0:
            print('ID'+10*' ','name'+10*' ','gender'+10*' ','salary')
            for i in r:
                print(str(i[0])+8*' ',i[1]+10*' ',i[2]+13*' ',i[3])
        else:
            print("employee with emp ID {} doesnt exist".format(ID))
        ans=input('enter y if want to continue search :')
display()
