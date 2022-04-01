import pymysql

con=pymysql.connect(host='bspxvqia9n5bvu0dkdle-mysql.services.clever-cloud.com',user='usiwf9f6sejtxk1w',password='W9n86OMTC0sSqE3TaVDr',database='bspxvqia9n5bvu0dkdle')
curs=con.cursor()

nm=input("enter ModelName of mobile: ")
curs.execute("select * from MOBILES where ModelName='%s'" %nm)
data=curs.fetchall()

if data:
    print(data)
else:
    print("not found")    
    

con.close()
